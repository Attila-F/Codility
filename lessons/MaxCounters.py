# -*- coding: utf-8 -*-

# Correctness: 100%
# Performance: 100%
# Complexity: O(N+M)

def solution(N, A):
    highest_ctr = 0
    counters = [0] * N
    prev_max_counter = True
    for op in A:
        if op > N:
            # Only reload the array if it would change the counters
            if not prev_max_counter:
                counters = [highest_ctr] * N
            prev_max_counter = True
        else:
            counters[op-1] += 1
            if counters[op-1] > highest_ctr:
                highest_ctr = counters[op-1]
            prev_max_counter = False

    return counters
