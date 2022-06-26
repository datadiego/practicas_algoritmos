import unittest
import random
randint = random.randint
import bubble_sort_function
sort = bubble_sort_function.bubble_sort

class test_bubble_sort(unittest.TestCase):
    def test_bubble_sort(self):
        arr_0 = [32, 1, 6, 9, 12, 88, 92, 54, 11, 10, 3, 4, 31, 100, 47]
        test0 = sort(arr_0)
        self.assertEqual(test0, [1, 3, 4, 6, 9, 10, 11, 12, 31, 32, 47, 54, 88, 92, 100])

        arr_1 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(sort(arr_1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        
if __name__ == '__main__':
    unittest.main()
