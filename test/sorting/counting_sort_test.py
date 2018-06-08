'''
Created on Apr 26, 2018

@author: vladimirfux
'''
import unittest

from sorting.counting import sort

class Test(unittest.TestCase):


    def testSingleElementSort(self):
        # set
        array = [1]
        k = 1
        # act
        result = sort(array, k)
        # assert
        self.assertEqual(result, [1], "Should return the same array")        
        
    def testTwoElementSort(self):
        # set
        array = [2, 1]
        k = 2
        # act
        result = sort(array, k)
        # assert
        self.assertEqual(result, [1, 2], "Should return sorted array")       

    
    def testFourElementSortWithMissingElement(self):
        # set
        array = [6, 1, 20, 10]
        k = 20
        # act
        result = sort(array, k)
        # assert
        self.assertEqual(result, [1, 6, 10, 20], "Should return sorted array")       
            
    def testWrongKRaisesError(self):
        array = [2, 1]
        k = 1
        # act       
        # assert
        with self.assertRaises(ValueError):
            sort(array, k)
            
    def testSortKeyedCollection(self):
        # setup
        class ObjectToSort:
            def __init__(self, key, load):
                self.key = key
                self.load = load
        
        o4 = ObjectToSort(4, "Four")
        o1 = ObjectToSort(1, "One")
        o3 = ObjectToSort(3, "Three")
        
        array = [o4, o1, o3]
        
        # act
        result = sort(array, 4, key=lambda x: x.key)
        
        # assert
        self.assertEqual(result, [o1, o3, o4], "Not sorted with key collection")
        
        
        
        
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
