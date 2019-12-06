import unittest

from sort import insertion_sort, merge_sort, quick_sort

class TestInsertionSort(unittest.TestCase):

    def test_sort(self):
        array = [6, 2, 5, 8, 1, 3, 7, 9, 4, 0]
        self.assertEqual(insertion_sort(array), list(range(10)))

    def test_sort_odd_elements(self):
        array = [6, 2, 5, 8, 1, 3, 7, 4, 0]
        self.assertEqual(insertion_sort(array), list(range(9)))

    def test_none(self):
        array = None
        # one way to test for exceptions using a context manager
        with self.assertRaises(TypeError):
            insertion_sort(array)
        # another way to test for exceptions using a function
        self.assertRaises(TypeError, insertion_sort, array)

    def test_single_item_array(self):
        array = [6]
        self.assertEqual(insertion_sort(array), array)

class TestMergeSort(unittest.TestCase):

    def test_sort(self):
        array = [6, 2, 5, 8, 1, 3, 7, 9, 4, 0]
        self.assertEqual(merge_sort(array), list(range(10)))

    def test_sort_odd_elements(self):
        array = [6, 2, 5, 8, 1, 3, 7, 4, 0]
        self.assertEqual(merge_sort(array), list(range(9)))

    def test_none(self):
        array = None
        # one way to test for exceptions using a context manager
        with self.assertRaises(TypeError):
            merge_sort(array)
        # another way to test for exceptions using a function
        self.assertRaises(TypeError, merge_sort, array)

    def test_single_item_array(self):
        array = [6]
        self.assertEqual(merge_sort(array), array)

class TestQuickSort(unittest.TestCase):

    def test_sort(self):
        array = [6, 2, 5, 8, 1, 3, 7, 9, 4, 0]
        self.assertEqual(quick_sort(array), list(range(10)))

    def test_sort_odd_elements(self):
        array = [6, 2, 5, 8, 1, 3, 7, 4, 0]
        self.assertEqual(quick_sort(array), list(range(9)))

    def test_sort_two_elements(self):
        array = [6, 2]
        self.assertEqual(quick_sort(array), [2, 6])

    def test_sort_three_elements(self):
        array = [6, 2, 4]
        self.assertEqual(quick_sort(array), [2, 4, 6])

    def test_sort_four_elements(self):
        array = [6, 2, 4, 9]
        self.assertEqual(quick_sort(array), [2, 4, 6, 9])

    def test_none(self):
        array = None
        # one way to test for exceptions using a context manager
        with self.assertRaises(TypeError):
            quick_sort(array)
        # another way to test for exceptions using a function
        self.assertRaises(TypeError, quick_sort, array)

    def test_single_item_array(self):
        array = [6]
        self.assertEqual(quick_sort(array), array)
