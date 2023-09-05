#!/usr/bin/python3
"""Importing the module of unnitest to test 6-max_integer module."""

from unittest import TestCase
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(TestCase):
    """This module is based on performing various test for
        6-max_integer.
    """
    def test_max_int(self):
        """Testing for a max integer in the positive int."""
        list_int = [1, 2, 5, 8, 9]
        self.assertEqual(max_integer(list_int), 9)

    def test_max_int_negative(self):
        """Testing for a max integer in the negative."""
        list_int_negative = [-1, -2, -5, -3]
        self.assertEqual(max_integer(list_int_negative), -1)

    def test_max_int_in_both(self):
        """Testing for a "max int in both positive and negative."""
        list_int_negative = [-1, 2, -5, -3]
        self.assertEqual(max_integer(list_int_negative), 2)

    def test_max_val(self):
        """Testing for a "max int in both positive and negative."""
        list_int = []
        self.assertEqual(max_integer(list_int), None)

    def test_max_character(self):
        """Testing a character in a string"""
        new_text = "Lazy dog"
        self.assertEqual(max_integer(new_text), 'z')

    def test_max_string(self):
        """Testing from the list of words"""
        new_text = ["Lazy", "Dog", "Read"]
        self.assertEqual(max_integer(new_text), 'Read')

    def text_max_int(self):
        """Testing in a in a list with single element"""
        new_list = [3]
        self.assertEqual((max_integer(new_list)), 3)
