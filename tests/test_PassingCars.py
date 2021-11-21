# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append("..")

from Codility.lessons.PassingCars import solution

example_test_cases = [
    (5, [0, 1, 0, 1, 1])
]

# N range: [1..100,000];
# Elements of a A: [0, 1]
# −1 if the number of pairs exceeds 1,000,000,000
extreme_test_cases = [
    (int(1e5), [0] + [1]*int(1e5)),
    (-1, [0]*5*int(1e4) + [1]*5*int(1e4))
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
