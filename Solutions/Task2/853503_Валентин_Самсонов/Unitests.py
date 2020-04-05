import unittest
import Sort
import Decorator
import Vector
import JSON
import random


class SortingTest(unittest.TestCase):
    def test_file_sorted(self):
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


class CacheTest(unittest.TestCase):
    def test_cached_sub(self):
        self.assertEqual(int(Decorator.fib(10)), 55)

    def test_cached_multi(self):
        self.assertEqual(int(Decorator.fib(20)), 6765)


class JSONTest(unittest.TestCase):
    data = JSON.JsonFormat()
    def test_list_convert(self):
        self.assertTrue(self.data.JsonConvert([1, 2, 3.6, "str", True, False, None, JSON.my_car])
                        == "[ 1, 2, 3.6, 'str', True, False, None, { 'Car':{ 'mark':'Mercedes', 'number':4356 } } ]")

    def test_class_convert(self):
        self.assertTrue(self.data.JsonConvert(JSON.my_car)
                        == "{ 'Car':{ 'mark':'Mercedes', 'number':4356 } }")



class VectorTest(unittest.TestCase):
    def test_multi(self):
        self.assertEqual(Vector.testvec1.scalarVector(Vector.testvec1, Vector.testvec2), 10)

    def test_vector_format(self):
        with self.assertRaises(TypeError):
            print(Vector.Vector([1, 2, 3]- 2))


unittest.main()
