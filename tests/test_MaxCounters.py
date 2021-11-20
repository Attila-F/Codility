# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append("..")

from Codility.lessons.MaxCounters import solution

example_test_cases = [
    # Solution, number of counters, sequence input
    ([3, 2, 2, 4, 2], 5, [3, 4, 4, 6, 1, 4, 4])
]

extreme_test_cases = [
    ([1e5] + [0]*(int(1e5)-1), int(1e5), [1]*int(1e5)),
    ([0]*(int(1e5)), int(1e5), [int(1e5)+1]*int(1e5))  # All max_counter operations
]

class TestColution(unittest.TestCase):
    def test_example(self):
        for test_case in example_test_cases:
            (S, N, A) = test_case
            self.assertEqual(S, solution(N, A))

    def test_example2(self):
        for test_case in extreme_test_cases:
            (S, N, A) = test_case
            self.assertEqual(S, solution(N, A))