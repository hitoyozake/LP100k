# -* encoding: utf-8 *-

import unittest
import section1
from section2 import section2

class TestKnock(unittest.TestCase):

    def test_section1(self):
        self.assertEqual(section1.problem_00(), "desserts")
        self.assertEqual(section1.problem_01(), "パトカー")
        self.assertEqual(section1.problem_02(), "パタトクカシーー")
        self.assertEqual(section1.problem_07(1, 2, 3), '1時の2は3')

        # self.assertEqual(section2.problem_10(), 24)
