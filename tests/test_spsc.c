#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <inttypes.h>
#include <pthread.h>
#include <string.h>

#include "../spsc_ring.h"

SPSC_RING_DECLARE(u64_ring, uint64_t)

static int tests_run = 0;
static int tests_failed = 0;

#define RUN_TEST(fn) do { \
    ++tests_run; \
    int _rc = fn(); \
    if (_rc != 0) { \
        ++tests_failed; \
        fprintf(stderr, "[FAIL] %s (rc=%d)\n", #fn, _rc); \
    } else { \
        fprintf(stdout, "[ OK ] %s\n", #fn); \
    } \
} while (0)

#define ASSERT_EQ_U64(a,b) do { \
    if ((uint64_t)(a) != (uint64_t)(b)) { \
        fprintf(stderr, "Assertion failed: %s == %s (%" PRIu64 " != %" PRIu64 ") at %s:%d\n", #a, #b, (uint64_t)(a), (uint64_t)(b), __FILE__, __LINE__); \
        return 1; \
    } \
} while (0)

#define ASSERT_TRUE(cond) do { \
    if (!(cond)) { \
        fprintf(stderr, "Assertion failed: %s at %s:%d\n", #cond, __FILE__, __LINE__); \
        return 1; \
    } \
} while (0)

static int test_basic_small(void) {
    u64_ring q; int rc = u64_ring_init(&q, 8); if (rc) return rc;
    for (uint64_t i = 1; i <= 4; ++i) {
        ASSERT_TRUE(u64_ring_try_enqueue(&q, i));
    }
    for (uint64_t i = 1; i <= 4; ++i) {
        uint64_t v = 0; ASSERT_TRUE(u64_ring_try_dequeue(&q, &v)); ASSERT_EQ_U64(v, i);
    }
    uint64_t tmp; ASSERT_TRUE(!u64_ring_try_dequeue(&q, &tmp));
    u64_ring_free(&q);
    return 0;
}

static int test_wrap_behavior(void) {
    u64_ring q; int rc = u64_ring_init(&q, 8); if (rc) return rc;
    for (uint64_t i = 1; i <= 6; ++i) ASSERT_TRUE(u64_ring_try_enqueue(&q, i));
    for (uint64_t i = 1; i <= 3; ++i) { uint64_t v; ASSERT_TRUE(u64_ring_try_dequeue(&q, &v)); ASSERT_EQ_U64(v, i); }
    for (uint64_t i = 7; i <= 10; ++i) ASSERT_TRUE(u64_ring_try_enqueue(&q, i));
    for (uint64_t i = 4; i <= 10; ++i) { uint64_t v; ASSERT_TRUE(u64_ring_try_dequeue(&q, &v)); ASSERT_EQ_U64(v, i); }
    u64_ring_free(&q);
    return 0;
}

static int test_burst_ops(void) {
    u64_ring q; int rc = u64_ring_init(&q, 16); if (rc) return rc;
    uint64_t in[12]; for (uint64_t i = 0; i < 12; ++i) in[i] = i + 1;
    size_t enq = u64_ring_enqueue_burst(&q, in, 12); ASSERT_EQ_U64(enq, 12);
    uint64_t out[12]; size_t deq = u64_ring_dequeue_burst(&q, out, 12); ASSERT_EQ_U64(deq, 12);
    for (uint64_t i = 0; i < 12; ++i) ASSERT_EQ_U64(out[i], in[i]);
    u64_ring_free(&q);
    return 0;
}

static int test_full_and_empty(void) {
    u64_ring q; int rc = u64_ring_init(&q, 8); if (rc) return rc;
    ASSERT_EQ_U64(u64_ring_capacity(&q), 8);
    uint64_t v;
    ASSERT_TRUE(!u64_ring_try_dequeue(&q, &v));
    for (uint64_t i = 0; i < 8; ++i) ASSERT_TRUE(u64_ring_try_enqueue(&q, i));
    ASSERT_TRUE(!u64_ring_try_enqueue(&q, 9));
    for (uint64_t i = 0; i < 8; ++i) ASSERT_TRUE(u64_ring_try_dequeue(&q, &v));
    ASSERT_TRUE(!u64_ring_try_dequeue(&q, &v));
    u64_ring_free(&q);
    return 0;
}

typedef struct {
    u64_ring* ring;
    uint64_t count;
} prod_args_t;

typedef struct {
    u64_ring* ring;
    uint64_t count;
    volatile uint64_t sum;
} cons_args_t;

#if defined(__x86_64__) || defined(__i386__)
static inline void cpu_relax(void) { __asm__ __volatile__("pause" ::: "memory"); }
#else
static inline void cpu_relax(void) { (void)0; }
#endif

static void* producer(void* arg) {
    prod_args_t* a = (prod_args_t*)arg;
    for (uint64_t i = 1; i <= a->count; ++i) {
        while (!u64_ring_try_enqueue(a->ring, i)) { cpu_relax(); }
    }
    return NULL;
}

static void* consumer(void* arg) {
    cons_args_t* a = (cons_args_t*)arg;
    uint64_t sum = 0;
    for (uint64_t i = 1; i <= a->count; ++i) {
        uint64_t v;
        while (!u64_ring_try_dequeue(a->ring, &v)) { cpu_relax(); }
        sum += v;
    }
    a->sum = sum;
    return NULL;
}

static int test_concurrency_correctness(void) {
    u64_ring q; int rc = u64_ring_init(&q, 1u << 16); if (rc) return rc;
    const uint64_t n = 1000000ull; /* 1M */
    prod_args_t pa = { .ring = &q, .count = n };
    cons_args_t ca = { .ring = &q, .count = n, .sum = 0 };
    pthread_t pt, ct;
    if (pthread_create(&pt, NULL, producer, &pa) != 0) return 1;
    if (pthread_create(&ct, NULL, consumer, &ca) != 0) return 1;
    pthread_join(pt, NULL);
    pthread_join(ct, NULL);
    unsigned __int128 expect = (unsigned __int128)n * (n + 1ull) / 2ull;
    ASSERT_TRUE((unsigned __int128)ca.sum == expect);
    u64_ring_free(&q);
    return 0;
}

int main(void) {
    RUN_TEST(test_basic_small);
    RUN_TEST(test_wrap_behavior);
    RUN_TEST(test_burst_ops);
    RUN_TEST(test_full_and_empty);
    RUN_TEST(test_concurrency_correctness);

    if (tests_failed == 0) {
        printf("\nAll %d tests passed.\n", tests_run);
        return 0;
    } else {
        printf("\n%d/%d tests failed.\n", tests_failed, tests_run);
        return 1;
    }
}

