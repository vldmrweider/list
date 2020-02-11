import unittest
from list.list import List


class TestList(unittest.TestCase):
    def test_first(self):
        test_list = List(1, 2, 3)
        self.assertEqual(str(List.get_normal_order(test_list)), "1 2 3")

    def test_second(self):
        test_list = List(1, 2, 3)
        test_list.append(4)
        assert str(List.get_normal_order(test_list)) == "1 2 3 4"

    def test_third(self):
        test_list = List(1, 2, 3, 4)
        tail_list = List(5, 6)
        test_list += tail_list
        assert str(List.get_normal_order(test_list)) == "1 2 3 4 5 6"

    def test_forth(self):
        test_list = List()
        assert str(test_list) == ""

    def test_fifth(self):
        test_list = List(None)
        assert str(test_list) == "None"

    def test_sixth(self):
        test_list = List(1, 2, 3)
        test_list += [4, 5]
        assert str(List.get_normal_order(test_list)) == "1 2 3 4 5"

    def test_reverse(self):
        test_list = List(1, 2, 3, 4, 5, 6)
        assert str(test_list) == "6 5 4 3 2 1"


if __name__ == '__main__':
    unittest.main()
