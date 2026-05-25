import unittest
import list_problems


class TestAltsFunction(unittest.TestCase):
    def test_odd_length(self):
        self.assertEqual([0, 2, 4], list_problems.alts([0, 1, 2, 3, 4]))

    def test_even_length(self):
        self.assertEqual([1, 3, 5], list_problems.alts([1, 2, 3, 4, 5, 6]))

    def test_zero_length_list(self):
        self.assertEqual([], list_problems.alts([]))


class TestFindFunction(unittest.TestCase):
    def test_element_in_front(self):
        self.assertEqual(0, list_problems.find([1, 2, 3], 1))

    def test_element_in_back(self):
        self.assertEqual(3, list_problems.find([1, 2, 3, 5], 5))

    def test_element_in_middle(self):
        self.assertEqual(2, list_problems.find([1, 2, 3, 5, 6], 3))

    def test_element_not_in_list(self):
        self.assertEqual(-1, list_problems.find([1, 2, 3, 4, 5], 17))

    def test_empty_list(self):
        self.assertEqual(-1, list_problems.find([], 1))


class TestLargestFunction(unittest.TestCase):
    def test_largest_in_front(self):
        self.assertEqual(14, list_problems.largest([14, 3, 5, 7]))

    def test_largest_in_back(self):
        self.assertEqual(7, list_problems.largest([1, 3, 5, 7]))

    def test_largest_in_middle(self):
        self.assertEqual(45, list_problems.largest([14, 3, 45, 5, 7]))

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            list_problems.largest([])


class TestReverseFunction(unittest.TestCase):
    def test_even_sized_list(self):
        lst = [1, 2, 3, 4]
        list_problems.reverse(lst)
        self.assertEqual([4, 3, 2, 1], lst)

    def test_odd_sized_list(self):
        lst = [1, 2, 3]
        list_problems.reverse(lst)
        self.assertEqual([3, 2, 1], lst)

    def test_size_one_list(self):
        lst = [1]
        list_problems.reverse(lst)
        self.assertEqual([1], lst)

    def test_empty_list(self):
        lst = []
        list_problems.reverse(lst)
        self.assertEqual([], lst)


class TestSortedFunction(unittest.TestCase):
    def test_unsorted_list(self):
        self.assertEqual(False, list_problems.sorted([3, 2, 5]))

    def test_sorted_list(self):
        self.assertEqual(True, list_problems.sorted([1, 2, 3]))

    def test_size_one_list(self):
        self.assertEqual(True, list_problems.sorted([5]))

    def test_empty_list(self):
        self.assertEqual(True, list_problems.sorted([]))


if __name__ == "__main__":
    unittest.main()
