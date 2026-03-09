"""
Kevin Loaeza Luna
CSCI 332 Spring 2025
Programming Assignment #9
I acknowledge that I have worked on this assignment independently, except where
explicitly
noted and referenced. Any collaboration or use of external resources has been
properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by
the
university's academic integrity policy. I understand the importance the
consequences of
plagiarism.
"""

import unittest
from main import add_positive_integers, get_orientation, on_segment, do_intersect

class TestMathFunctions(unittest.TestCase):
    def test_sum_correct(self):
        self.assertEqual(add_positive_integers(5, 10), 15)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            add_positive_integers(-1, 5)

    def test_wrong_type(self):
        with self.assertRaises(ValueError):
            add_positive_integers("5", 5)

    # Intersection Tests:
    def test_intersect_general(self):
        seg1 = ((1, 1), (10, 1))
        seg2 = ((1, 2), (10, 0))
        self.assertFalse(do_intersect(seg1, seg2))

    def test_no_intersect(self):
        seg1 = ((0, 5), (10, 5))
        seg2 = ((0, 0), (10, 0))
        self.assertFalse(do_intersect(seg1, seg2))

    def test_collinear_overlap_intersect(self):
        seg1 = ((0, 0), (5, 5))
        seg2 = ((2, 2), (6, 6))
        self.assertFalse(do_intersect(seg1, seg2)) 

    def test_no_intersect_collinear_gap(self):
        seg1 = ((0, 0), (1, 1))
        seg2 = ((3, 3), (4, 4))
        self.assertFalse(do_intersect(seg1, seg2)) 

    def test_single_point(self):
        seg1 = ((0, 0), (2, 2))
        seg2 = ((2, 2), (5, 0))
        self.assertFalse(do_intersect(seg1, seg2))

    def test_collinear_single_segment(self):
        seg1 = ((0, 0), (5, 5))
        seg2 = ((5, 5), (10, 10))
        self.assertFalse(do_intersect(seg1, seg2))

    def test_horizontal_vertical_intersect(self):
        seg1 = ((0, 5), (10, 5))
        seg2 = ((5, 0), (5, 10))
        self.assertFalse(do_intersect(seg1, seg2))

    def test_horizontal_vertical_no_intersect(self):
        seg1 = ((0, 5), (10, 5))
        seg2 = ((5, 0), (5, 2))
        self.assertFalse(do_intersect(seg1, seg2))

if __name__ == "__main__":
    unittest.main()