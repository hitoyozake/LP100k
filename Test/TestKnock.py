# -* encoding: utf-8 *-

import unittest
import section1

class TestKnock(unittest.TestCase):

    def test_section1(self):

        self.assertEqual(section1.problem_00(), "desserts")