'''
Created on May 3, 2018

@author: vladimirfux
'''
import unittest

from sorting.radix import sort, get_digit, sort_by_digit
class Test(unittest.TestCase):



        
    def testIfWorksForSingleElementWithWrongDigit(self):
        # setup
        array = [123]
        d = 10
        
        # act
        result = sort(array, d)
        
        # assert
        self.assertEqual(result, [123], 'Should return exactly the same array')
    
    
    def testIfWorksForTwoElementsDesc(self):
        # setup
        array = [123, 11]
        d = 3
        
        # act
        result = sort(array, d)
        
        # assert
        self.assertEqual(result, [11, 123], 'Should return sorted ASC array but returns ' + str(result))
        
        
    def testIfDigitsReturnCorrect(self):
        num = 196234
        
        self.assertEqual(get_digit(num, 3), 2, "Incorrect digit returned " + str(get_digit(num, 3)))
        
    def testIfDigitsMoreThanRealReturnZero(self):
        num = 1962
        
        self.assertEqual(get_digit(num, 10), 0, "Incorrect digit returned " + str(get_digit(num, 10)))
        
    def testIfSortByDigitWorks(self):
        # setup
        array = [543, 123, 654]
        
        # act
        result = sort_by_digit(array, 2)
        print()
        # assert
        self.assertEqual(result, [123, 543, 654], "Sort by digit returns wrong array: " + str(result))
        
        
            
    def testIfSortByWorks(self):
        # setup
        array = [543, 123, 654, 1, 23, 0, 1000]
        
        # act
        result = sort(array, 4)
        # assert
        self.assertEqual(result, [0, 1, 23, 123, 543, 654, 1000], "Sort by digit returns wrong array: " + str(result))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testIfWorksForSingleElement']
    unittest.main()
