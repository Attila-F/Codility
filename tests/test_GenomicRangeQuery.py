# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append("..")

from Codility.lessons.GenomicRangeQuery import solution

example_test_cases = [
    ([2, 4, 1], 'CAGCCTA',  [2, 5, 0], [4, 5, 6])
]

# S range: ['A', 'C', 'G', 'T'] of N elements
# N range: [1..100,000]
# P[K] and Q[K] range of M elements: [0..N-1], P[K] <= Q[K], 0 ≤ K < M
# M range: [1..50,000]
extreme_test_cases = [
    ([1, 2]+[1]*49998, 'ACGT'*25000,  range(0, 50000), range(0, 100000, 2)),
]


class TestColution(unittest.TestCase):
    def test_example(self):
        for test_case in example_test_cases:
            (sol, S, P, Q) = test_case
            self.assertEqual(sol, solution(S, P, Q))

    def test_example2(self):
        for test_case in extreme_test_cases:
            (sol, S, P, Q) = test_case
            self.assertEqual(sol, solution(S, P ,Q))
