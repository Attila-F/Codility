# -*- coding: utf-8 -*-

def solution(A, B, K):
    # Find the smallest x >= A such that x % K == 0
    x = A + ((K - A%K) % K)

    # Find the largest y <= B such that y % K == 0
    y = B - (B%K)

    # Return the number of integers within the range [x..y] that are divisible by K
    return int((y - x) / K) + 1