import unittest
import Sort
import Decorator
import Vector
import JSON
import random


class SortingTest(unittest.TestCase):
    def find_if_file_can_be_sorted(self):
        with open('numbers.txt', 'w') as file:
            file.writelines('{}\n'.format(random.randint(1, 1000000)) for _ in range(int(100)))

        with self.assertRaises(Exception):
            Sort.externalSorting.fileSplitting("numbers.txt", 10)
            Sort.externalSorting.fileSorting()

    def test_sort(self):
        list1 = [8, 2, 23, 45, 14]
        list2 = list1
        Sort.externalSorting().sort(list2)
        self.assertEqual(list2, sorted(list1))


class CachedTest(unittest.TestCase):
    def test_cached_sub(self):
        self.assertEqual(int(Decorator.sub(10, 7)), 3)

    def test_cached_multi(self):
        self.assertEqual(int(Decorator.multi(3, 2)), 6)


class JSONTest(unittest.TestCase):
    def text_JSON_string(self):
        self.assertTrue(JSON.toJSON("Valera", "Karpin", "Opel"), str)

    def test_incomplete(self):
        with self.assertRaises(TypeError):
            user = JSON.User("Max")


class VectorTest(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(Vector.Vector([1, 2, 2], 3).lenVector(), 3)

    def test_plus_not_vector(self):
        with self.assertRaises(TypeError):
            print(Vector.Vector([1, 2, 3], 3) - 2)


unittest.main()
