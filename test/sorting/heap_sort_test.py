'''
Created on May 7, 2018

@author: vladimirfux
'''
import unittest
from numpy.ma.testutils import assert_equal
import sorting.heap as hp

class Test(unittest.TestCase):


    def testLeftReturnsSecond(self):
        # setup
        array = [1, 2, 3]
        
        # assert
        assert_equal(hp.left(array, 0), 2)

    def testLeftOnNoChildReturnsNone(self):
        # setup
        array = [1, 2, 3]        
        # assert
        assert_equal(hp.left(array, 1), None)
        assert_equal(hp.left(array, 2), None)
        
        
    def testRightReturnsThird(self):
        # setup
        array = [1, 2, 3]
        
        # assert
        assert_equal(hp.right(array, 0), 3)    
        
    def testIfParentReturnsRootOnChild(self):
        # setup
        array = [1, 2, 3]        
        # assert
        assert_equal(hp.parent(array, 1), 1)
        
        
    def testIfParentReturnsNoneOnRoot(self):
        # setup
        array = [1, 2, 3]        
        # assert
        assert_equal(hp.parent(array, 0), None)
        
        
    def testIfHeapIsHeap(self):
        # setup
        array = [10, 4, 6, 2, 2, 3, 4, 1]        
        # assert
        assert_equal(hp.is_heap(array), True)    
        
    def testIfHeapIsNotHeap(self):
        # setup
        array = [10, 12, 6, 2, 2, 3, 4, 1]        
        # assert
        assert_equal(hp.is_heap(array), False)    
        
    def testIfHeapifyReturnsHeapOnTwoElements(self):      
        # setup
        array = [1, 2]
        
        # act 
        hp.heapify(array, 0)
        
        # assert
        assert_equal(array, [2, 1])
        
        
    def testIfBuildedHeapIsHeap(self):
        # setup
        array = [3, 1, 5, 6, 1, 2, 6, 2, 5]
        
        # act
        hp.build_heap(array)

        # assert
        self.assert_(hp.is_heap(array))   
        
        
    
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testLeftReturnsRoot']
    unittest.main()
