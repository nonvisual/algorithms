'''
Created on Apr 18, 2018

@author: vladimirfux
'''
import unittest
from sorting.quick import QuickSort
from random import randint,seed

class QuickSortTest(unittest.TestCase):

    def set_up(self):
        seed(12341)
        
    def test_pivot_two_elements(self):
        array = [2,1]
        QuickSort.pivot(array, 0, 1, 1)
        self.assert_(array[1]==2 and array[0]==1)
        
    def test_pivot_three_elements(self):
        array = [1,3,2]
        p_index = QuickSort.pivot(array, 0, 2, 2)
        self.assert_(array[1]==2 and array[0]==1 and p_index==1)

    def test_pivot_five_elements(self):
        array = [7,4,5,3,1]
        p_index = QuickSort.pivot(array, 0, 4, 1)
        self.assert_(array[2]==4 and array[0]<4 and array[1]<4  and p_index==2)  
    
    def test_pivot_all_to_right(self):
        array = [9,8,7,6,5,4,1]
        p_index = QuickSort.pivot(array, 0, 6, 6)
        self.assert_(array[0]==1  and p_index==0)    
        
    def test_pivot_all_to_left(self):
        array = [10,9,8,7,6,5,4]
        p_index = QuickSort.pivot(array, 0, 6, 0)
        self.assert_(array[6]==10  and p_index==6)  
        
    def test_sort_desc(self):
        array = [10, 9, 8, 7, 6, 5, 4]
        QuickSort.sort(array, 0, 6)
        self.assert_(array == [4, 5, 6, 7, 8, 9, 10])  
    
    def test_sort_asc(self):
        array = [1,2,3,4,5,6,7,8]
        QuickSort.sort(array, 0, 7)
        self.assert_(array == [1,2,3,4,5,6,7,8])  
    
    def test_sort_ran(self):
        array = [3,62,1,4,12,262,3,61,2,6]
        QuickSort.sort(array, 0, 9)
        self.assert_(array == [1,2,3,3,4,6,12,61,62,262])  
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
