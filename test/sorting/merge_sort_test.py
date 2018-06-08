'''
Created on Apr 18, 2018

@author: vladimirfux
'''
import unittest
from sorting.merge import MergeSort


class MergeSortTest(unittest.TestCase):

    def test_merge_two_elements(self):
        array = [2, 1]
        MergeSort.merge(array, 0, 1, 0)
        self.assertEqual(array, [1, 2], "[1,2] as the merge result should be returned")

        
    def test_merge_several_elements(self):
        array = [2, 5, 6, 1, 2, 3]
        MergeSort.merge(array, 0, 5, 2)
        self.assertEqual(array, [1, 2, 2, 3, 5, 6], "[1, 2, 2, 3, 5, 6] as the merge result should be returned")



    def test_sort_single_element(self):
        array = [1]
        MergeSort.sort(array, 0, 0)
        self.assertEqual(array, [1], "single element array should be returned")
        
    def test_sort_two_elements(self):
        array = [2, 1]
        MergeSort.sort(array, 0, 1)
        self.assertEqual(array, [1, 2], "")
        
    def test_sort_desc(self):
        array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        MergeSort.sort(array, 0, 8)
        self.assertEqual(array, [1, 2, 3, 4, 5, 6, 7, 8, 9], "array is sorted incorrectly")
    
    def test_sort_asc(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        MergeSort.sort(array, 0, 8)
        self.assertEqual(array, [1, 2, 3, 4, 5, 6, 7, 8, 9], "array is sorted incorrectly")    
        


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testSortSingleElement']
    unittest.main()
