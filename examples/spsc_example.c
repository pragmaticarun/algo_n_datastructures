#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <pthread.h>
#include <time.h>
#include <errno.h>
#include <string.h>

#include "../spsc_ring.h"

SPSC_RING_DECLARE(u64_ring, uint64_t)

typedef struct {
    u64_ring* ring;
    uint64_t count;
} producer_args_t;

typedef struct {
    u64_ring* ring;
    uint64_t count;
    volatile uint64_t sum;
} consumer_args_t;

static inline uint64_t now_ns(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (uint64_t)ts.tv_sec * 1000000000ull + (uint64_t)ts.tv_nsec;
}

#if defined(__x86_64__) || defined(__i386__)
static inline void cpu_relax(void) { __asm__ __volatile__("pause" ::: "memory"); }
#else
static inline void cpu_relax(void) { (void)0; }
#endif

void* producer_thread(void* arg) {
    producer_args_t* pargs = (producer_args_t*)arg;
    u64_ring* ring = pargs->ring;
    for (uint64_t i = 1; i <= pargs->count; ++i) {
        while (!u64_ring_try_enqueue(ring, i)) {
            cpu_relax();
        }
    }
    return NULL;
}

void* consumer_thread(void* arg) {
    consumer_args_t* cargs = (consumer_args_t*)arg;
    u64_ring* ring = cargs->ring;
    uint64_t sum = 0;
    for (uint64_t i = 1; i <= cargs->count; ++i) {
        uint64_t v;
        while (!u64_ring_try_dequeue(ring, &v)) {
            cpu_relax();
        }
        sum += v;
    }
    cargs->sum = sum;
    return NULL;
}

int main(int argc, char** argv) {
    const uint64_t n = (argc > 1) ? strtoull(argv[1], NULL, 10) : 50000000ull;
    const size_t capacity = (argc > 2) ? strtoull(argv[2], NULL, 10) : (1u << 20); /* 1M */

    u64_ring ring;
    int rc = u64_ring_init(&ring, capacity);
    if (rc != 0) {
        fprintf(stderr, "ring init failed: %s\n", strerror(rc));
        return 1;
    }

    pthread_t prod, cons;
    producer_args_t pargs = { .ring = &ring, .count = n };
    consumer_args_t cargs = { .ring = &ring, .count = n, .sum = 0 };

    uint64_t t0 = now_ns();
    if (pthread_create(&prod, NULL, producer_thread, &pargs) != 0) {
        perror("pthread_create(prod)");
        return 1;
    }
    if (pthread_create(&cons, NULL, consumer_thread, &cargs) != 0) {
        perror("pthread_create(cons)");
        return 1;
    }

    pthread_join(prod, NULL);
    pthread_join(cons, NULL);
    uint64_t t1 = now_ns();

    const long double sec = (long double)(t1 - t0) / 1e9L;
    const long double mops = (long double)n / 1e6L / sec;
    const unsigned __int128 expect = (unsigned __int128)n * (n + 1ull) / 2ull;

    printf("Processed %" PRIu64 " items in %.3Lf s -> %.2Lf Mops/s\n", n, sec, mops);
    printf("Sum: %" PRIu64 ", Expected: %llu\n", (uint64_t)cargs.sum, (unsigned long long)expect);

    if ((unsigned __int128)cargs.sum != expect) {
        fprintf(stderr, "Validation failed!\n");
        return 2;
    }

    u64_ring_free(&ring);
    return 0;
}

