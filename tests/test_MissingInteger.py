# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append("..")

from Codility.lessons.MissingInteger import solution

# A = [1, 3, 6, 4, 1, 2], the function should return 5.
example_test_cases = [
    (5, [1, 3, 6, 4, 1, 2]),
    (4, [1, 2, 3]),
    (1, [-1, -3])
]

# N range: [1..100,000];
# Elements of A range: [−1,000,000..1,000,000].
extreme_test_cases = [
    (int(1e5), range(int(1e5)))
]

class TestColution(unittest.TestCase):
    def test_example(self):
        for test_case in example_test_cases:
            (S, A) = test_case
            self.assertEqual(S, solution(A))

    def test_example2(self):
        for test_case in extreme_test_cases:
            (S, A) = test_case
            self.assertEqual(S, solution(A))