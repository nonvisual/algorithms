'''
Created on May 18, 2018

@author: vladimirfux
'''
import unittest
from data_structures.red_black_tree import RedBlackTree,Color

class Test(unittest.TestCase):

    def setUp(self):
        self.bt = RedBlackTree()
        
        
    def testIfAddSetsRoot(self):
        # setup
        
        
        # act
        self.bt.insert(1, "v")
        
        # assert        
        self.assert_(self.bt.root != None, "Root should be not null")
        self.assert_(self.bt.search(1).value == "v", "Value should be returned")

        
    def testIfSearchOnEmptyTreeIsNone(self):

        # assert      
        self.assert_(self.bt.search(1) == None, "Empty tree should return None")
        
    
    def testIfTwoElementTreeIsOredered(self):
       
        # act
        self.bt.insert(2, "v")
        self.bt.insert(1, "j")
        
        # assert
        self.assert_(self.bt.ordered_values() == ["j", "v"], "Should return ordered set, not " + str(self.bt.ordered_values()))    

    
    def testIfSuccessorOfSingleElementIsNone(self):

        # act
        self.bt.insert(2, "v")
        
        # assert        
        self.assert_(self.bt.successorByKey(2) == None, "No successor")    
        
    def testIfSuccessorOfTwoElementsIsLargest(self):

        # act
        self.bt.insert(2, "v")
        self.bt.insert(3, "j")

        # assert        
        self.assert_(self.bt.successorByKey(2).key == 3, "Should return successor")      
        self.assert_(self.bt.successorByKey(3) == None, "Should return no successor") 
        self.assert_(self.__check_black_height(self.bt.root)!=-1, "Black height property is violated")

    def testIfSuccessorWithNoChildWorks(self):

        # act
        self.bt.insert(5, "a")
        self.bt.insert(2, "v")
        self.bt.insert(3, "j")

        # assert        
        self.assert_(self.bt.successorByKey(3).key == 5, "Should return successor")      
        self.assert_(self.__check_black_height(self.bt.root)!=-1, "Black height property is violated")

    def testIfBiggerTreeReturnsOrderedValues(self):


        # act
        self.bt.insert(5, "5")
        self.bt.insert(2, "2")
        self.bt.insert(3, "3")
        self.bt.insert(11, "11")
        self.bt.insert(0, "0")
        self.bt.insert(6, "6")
        self.bt.insert(8, "8")
        self.bt.insert(7, "7")
        
        # assert      
        self.assert_(self.bt.ordered_values() == ["0", "2", "3", "5", "6", "7", "8", "11"], "Should return ordered set")    
        self.assert_(self.__check_black_height(self.bt.root)!=-1, "Black height property is violated")

        
            
    def testIfDeleteCorrectlyWorksForTrickyCase(self):
        # setup
        self.bt.insert(8, "8")
        self.assert_(self.__check_black_height(self.bt.root)!=-1, "Black height property is violated")

        self.bt.insert(10, "10")
        self.assert_(self.__check_black_height(self.bt.root)!=-1, "Black height property is violated")
        self.bt.insert(9, "9")
        self.assert_(self.__check_black_height(self.bt.root)!=-1, "Black height property is violated")
        self.bt.insert(19, "19")
        self.assert_(self.__check_black_height(self.bt.root)!=-1, "Black height property is violated")
        self.bt.insert(21, "21")
        self.assert_(self.__check_black_height(self.bt.root)!=-1, "Black height property is violated")
        self.bt.insert(11, "11")
        self.assert_(self.__check_black_height(self.bt.root)!=-1, "Black height property is violated")
        self.bt.insert(17, "17")
        
        # act        
        self.bt.delete(10)
        
        # assert
        # 11 is left child of root
        self.assert_(self.bt.search(8).right_child.key == 11, "11 should take place of right child, not " + str(self.bt.root.right_child.key))
        ordered_keys = [node.key for node in  self.bt.ordered()]
        self.assert_(ordered_keys == [8, 9, 11, 17, 19, 21], "Ordering is violated: " + str(ordered_keys))
        self.assert_(self.__check_black_height(self.bt.root)!=-1, "Black height property is violated")

    '''
    Returns tree black height if all branches have the same height, -1 otherwise
    '''
    def __check_black_height(self, node):
        # empty leaf is BLACK
        if node == None:
            return 1
        left = self.__check_black_height(node.left_child)
        right = self.__check_black_height(node.right_child)
        result = -1
        if(left == right and left != -1):
            if node.color==Color.BLACK:
                result = left + 1
            else:
                result = left 
        
        return result

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
