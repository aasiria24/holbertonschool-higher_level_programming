#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test with max value at the beginning"""
        self.assertEqual(max_integer([5, 2, 3, 4]), 5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_identical_values(self):
        """Test with all identical values"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_floats(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 3.3, 4.9]), 4.9)

    def test_mixed_integers_floats(self):
        """Test with mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.2]), 4.2)

    def test_list_of_strings(self):
        """Test with a list of strings (if function should handle this)"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_none_input(self):
        """Test with None as input"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_list_input(self):
        """Test with non-list input"""
        with self.assertRaises(TypeError):
            max_integer(123)

if __name__ == '__main__':
    unittest.main()
