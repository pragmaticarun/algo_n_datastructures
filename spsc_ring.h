/*
 * spsc_ring.h - Header-only Single-Producer Single-Consumer lock-free circular queue
 *
 * Ultra-low-latency SPSC ring buffer using C11 atomics with cache-line separation
 * between producer and consumer indices to avoid false sharing.
 *
 * Usage:
 *   - Define a ring for a specific element type with SPSC_RING_DECLARE(MyRing, uint64_t)
 *   - Initialize with MyRing_init(&q, capacity);
 *     (capacity will be rounded up to the next power of two)
 *   - Enqueue/Dequeue with MyRing_try_enqueue / MyRing_try_dequeue
 *   - Use burst variants to minimize atomic ops when pushing/popping many items
 *   - Free with MyRing_free(&q)
 *
 * Threading model: exactly 1 producer thread, exactly 1 consumer thread.
 * Memory order:
 *   - Producer stores to elements, then publishes head with release store
 *   - Consumer observes head with acquire load before reading elements
 *   - Symmetric for tail publication and observation
 */

#ifndef SPSC_RING_H
#define SPSC_RING_H

#include <stdatomic.h>
#include <stdalign.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#ifndef SPSC_CACHELINE
#define SPSC_CACHELINE 64
#endif

_Static_assert(SPSC_CACHELINE >= sizeof(_Atomic size_t), "SPSC_CACHELINE too small for atomic size_t");

#if defined(__GNUC__) || defined(__clang__)
#define SPSC_LIKELY(x)   __builtin_expect(!!(x), 1)
#define SPSC_UNLIKELY(x) __builtin_expect(!!(x), 0)
#else
#define SPSC_LIKELY(x)   (x)
#define SPSC_UNLIKELY(x) (x)
#endif

#define SPSC_ALIGN_CACHELINE _Alignas(SPSC_CACHELINE)

/* Round up to next power of two, minimum 2 */
static inline size_t spsc_next_power_of_two(size_t value) {
    if (value < 2) {
        return 2u;
    }
    value--;
    for (size_t i = 1; i < (sizeof(size_t) * 8); i <<= 1) {
        value |= value >> i;
    }
    value++;
    return value;
}

/* Aligned allocation helper (64-byte alignment by default) */
static inline void* spsc_aligned_alloc(size_t alignment, size_t size) {
#if defined(_ISOC11_SOURCE) || (defined(__STDC_VERSION__) && __STDC_VERSION__ >= 201112L)
    /* aligned_alloc requires size to be a multiple of alignment */
    size_t rem = size % alignment;
    if (rem != 0) {
        size += (alignment - rem);
    }
    void* ptr = aligned_alloc(alignment, size);
    if (!ptr) {
        errno = ENOMEM;
    }
    return ptr;
#else
    void* ptr = NULL;
    if (posix_memalign(&ptr, alignment, size) != 0) {
        return NULL;
    }
    return ptr;
#endif
}

/* Define a strongly-typed SPSC ring for element TYPE with public name NAME. */
#define SPSC_RING_DECLARE(NAME, TYPE) \
typedef struct NAME { \
    struct { SPSC_ALIGN_CACHELINE _Atomic size_t head; char _pad_h[SPSC_CACHELINE - sizeof(_Atomic size_t)]; } _producer; \
    struct { SPSC_ALIGN_CACHELINE _Atomic size_t tail; char _pad_t[SPSC_CACHELINE - sizeof(_Atomic size_t)]; } _consumer; \
    size_t capacity; \
    size_t mask; \
    TYPE* buffer; \
} NAME; \
\
static inline int NAME##_init(NAME* q, size_t capacity) { \
    if (!q) { \
        return EINVAL; \
    } \
    size_t cap = spsc_next_power_of_two(capacity); \
    q->capacity = cap; \
    q->mask = cap - 1u; \
    q->buffer = (TYPE*) spsc_aligned_alloc(SPSC_CACHELINE, cap * sizeof(TYPE)); \
    if (SPSC_UNLIKELY(q->buffer == NULL)) { \
        q->capacity = 0; \
        q->mask = 0; \
        return ENOMEM; \
    } \
    atomic_store_explicit(&q->_producer.head, 0u, memory_order_relaxed); \
    atomic_store_explicit(&q->_consumer.tail, 0u, memory_order_relaxed); \
    return 0; \
} \
\
static inline void NAME##_free(NAME* q) { \
    if (!q) { \
        return; \
    } \
    free(q->buffer); \
    q->buffer = NULL; \
    q->capacity = 0; \
    q->mask = 0; \
    atomic_store_explicit(&q->_producer.head, 0u, memory_order_relaxed); \
    atomic_store_explicit(&q->_consumer.tail, 0u, memory_order_relaxed); \
} \
\
static inline size_t NAME##_capacity(const NAME* q) { \
    return q->capacity; \
} \
\
static inline size_t NAME##_size(const NAME* q) { \
    size_t head = atomic_load_explicit(&q->_producer.head, memory_order_acquire); \
    size_t tail = atomic_load_explicit(&q->_consumer.tail, memory_order_acquire); \
    return head - tail; \
} \
\
static inline bool NAME##_try_enqueue(NAME* q, TYPE value) { \
    size_t head = atomic_load_explicit(&q->_producer.head, memory_order_relaxed); \
    size_t tail = atomic_load_explicit(&q->_consumer.tail, memory_order_acquire); \
    if (SPSC_UNLIKELY((head - tail) == q->capacity)) { \
        return false; \
    } \
    q->buffer[head & q->mask] = value; \
    atomic_store_explicit(&q->_producer.head, head + 1u, memory_order_release); \
    return true; \
} \
\
static inline size_t NAME##_enqueue_burst(NAME* q, const TYPE* src, size_t count) { \
    size_t head = atomic_load_explicit(&q->_producer.head, memory_order_relaxed); \
    size_t tail = atomic_load_explicit(&q->_consumer.tail, memory_order_acquire); \
    size_t free_slots = q->capacity - (head - tail); \
    size_t n = (count < free_slots) ? count : free_slots; \
    if (SPSC_UNLIKELY(n == 0)) { \
        return 0; \
    } \
    size_t first = q->capacity - (head & q->mask); \
    if (first > n) first = n; \
    /* copy first segment */ \
    for (size_t i = 0; i < first; ++i) { \
        q->buffer[(head + i) & q->mask] = src[i]; \
    } \
    /* copy wrap-around segment */ \
    for (size_t i = 0; i < (n - first); ++i) { \
        q->buffer[(head + first + i) & q->mask] = src[first + i]; \
    } \
    atomic_store_explicit(&q->_producer.head, head + n, memory_order_release); \
    return n; \
} \
\
static inline bool NAME##_try_dequeue(NAME* q, TYPE* out) { \
    size_t tail = atomic_load_explicit(&q->_consumer.tail, memory_order_relaxed); \
    size_t head = atomic_load_explicit(&q->_producer.head, memory_order_acquire); \
    if (SPSC_UNLIKELY(tail == head)) { \
        return false; \
    } \
    *out = q->buffer[tail & q->mask]; \
    atomic_store_explicit(&q->_consumer.tail, tail + 1u, memory_order_release); \
    return true; \
} \
\
static inline size_t NAME##_dequeue_burst(NAME* q, TYPE* dst, size_t count) { \
    size_t tail = atomic_load_explicit(&q->_consumer.tail, memory_order_relaxed); \
    size_t head = atomic_load_explicit(&q->_producer.head, memory_order_acquire); \
    size_t avail = head - tail; \
    size_t n = (count < avail) ? count : avail; \
    if (SPSC_UNLIKELY(n == 0)) { \
        return 0; \
    } \
    size_t first = q->capacity - (tail & q->mask); \
    if (first > n) first = n; \
    for (size_t i = 0; i < first; ++i) { \
        dst[i] = q->buffer[(tail + i) & q->mask]; \
    } \
    for (size_t i = 0; i < (n - first); ++i) { \
        dst[first + i] = q->buffer[(tail + first + i) & q->mask]; \
    } \
    atomic_store_explicit(&q->_consumer.tail, tail + n, memory_order_release); \
    return n; \
}

#endif /* SPSC_RING_H */

