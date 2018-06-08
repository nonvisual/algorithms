'''
Created on May 16, 2018

@author: vladimirfux
'''
import unittest
from data_structures.binary_search_tree import BinaryTree, Node


class Test(unittest.TestCase):


    def testIfAddSetsRoot(self):
        # setup
        bt = BinaryTree()
        
        # act
        bt.insert(1, "v")
        
        # assert        
        self.assert_(bt.root != None, "Root should be not null")
        self.assert_(bt.search(1).value == "v", "Value should be returned")

        
    def testIfSearchOnEmptyTreeIsNone(self):
        # setup
        bt = BinaryTree()
        
        # assert      
        self.assert_(bt.search(1) == None, "Empty tree should return None")
        
    
    def testIfTwoElementTreeIsOredered(self):
        # setup
        bt = BinaryTree()
        
        # act
        bt.insert(2, "v")
        bt.insert(1, "j")
        
        # assert
        self.assert_(bt.ordered_values() == ["j", "v"], "Should return ordered set, not " + str(bt.ordered_values()))    

    
    def testIfSuccessorOfSingleElementIsNone(self):
        # setup
        bt = BinaryTree()
        
        # act
        bt.insert(2, "v")
        
        # assert        
        self.assert_(bt.successorByKey(2) == None, "No successor")    
        
    def testIfSuccessorOfTwoElementsIsLargest(self):
        # setup
        bt = BinaryTree()
        
        # act
        bt.insert(2, "v")
        bt.insert(3, "j")

        # assert        
        self.assert_(bt.successorByKey(2).key == 3, "Should return successor")      
        self.assert_(bt.successorByKey(3) == None, "Should return no successor") 
        
    def testIfSuccessorWithNoChildWorks(self):
        # setup
        bt = BinaryTree()
        
        # act
        bt.insert(5, "a")
        bt.insert(2, "v")
        bt.insert(3, "j")

        # assert        
        self.assert_(bt.successorByKey(3).key == 5, "Should return successor")      
        
    def testIfBiggerTreeReturnsOrderedValues(self):
        # setup
        bt = BinaryTree()
        
        # act
        bt.insert(5, "5")
        bt.insert(2, "2")
        bt.insert(3, "3")
        bt.insert(11, "11")
        bt.insert(0, "0")
        bt.insert(6, "6")
        bt.insert(8, "8")
        bt.insert(7, "7")
        
        # assert      
        self.assert_(bt.ordered_values() == ["0", "2", "3", "5", "6", "7", "8", "11"], "Should return ordered set")    
        
        
    def testIfTransplantationWorks(self):
        # setup
        bt = BinaryTree()
        
        # act
        bt.insert(9, "9")
        bt.insert(10, "10")
        bt.insert(19, "19")
        bt.insert(21, "21")
        bt.insert(11, "11")
        bt.insert(17, "17")
        
        bt.transplant(bt.search(19), bt.search(11))
        
        # assert
        self.assert_(bt.ordered_values() == ["9", "10", "11", "17"], "Should return transplanted set, not " + str(bt.ordered_values()))    

        
        
    def testIfDeleteCorrectlyWorksForTrickyCase(self):
        # setup
        bt = BinaryTree()
        bt.insert(8, "8")
        bt.insert(10, "10")
        bt.insert(9, "9")
        bt.insert(19, "19")
        bt.insert(21, "21")
        bt.insert(11, "11")
        bt.insert(17, "17")
        
        # act        
        bt.delete(10)
        
        # assert
        # 11 is left child of root
        self.assert_(bt.search(8).right_child.key == 11, "11 should take place of right child, not " + str(bt.root.right_child.key))
        ordered_keys = [node.key for node in  bt.ordered()]
        self.assert_(ordered_keys == [8, 9, 11, 17, 19, 21], "Ordering is violated: " + str(ordered_keys))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
