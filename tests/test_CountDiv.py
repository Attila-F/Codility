# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append("..")

from Codility.lessons.CountDiv import solution

# A = 6, B = 11 and K = 2, function should return 3
example_test_cases = [
    (3, 6, 11, 2)
]

# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.
extreme_test_cases = [
    (int(2*1e9)+1, 0, int(2*1e9), 1)
]


class TestColution(unittest.TestCase):
    def test_example(self):
        for test_case in example_test_cases:
            (S, A, B, K) = test_case
            self.assertEqual(S, solution(A, B, K))

    def test_example2(self):
        for test_case in extreme_test_cases:
            (S, A, B ,K) = test_case
            self.assertEqual(S, solution(A, B, K))
