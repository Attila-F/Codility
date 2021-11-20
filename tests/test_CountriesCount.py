# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append("..")

from Codility.exercises.CountriesCount import solution

test_cases = [
    (11, [[5, 4, 4], [4, 3, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4], [4, 1, 1]])
]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for testcase in test_cases:
            (countries, countrymap) = testcase
            result = solution(countrymap)
            self.assertEqual(countries, result)


if __name__ == "__main__":
    unittest.main()
