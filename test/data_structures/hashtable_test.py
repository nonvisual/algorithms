'''
Created on May 9, 2018

@author: vladimirfux
'''
import unittest

from data_structures.hashtable import Hashtable

class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.table = Hashtable() 


    def testIfHashtableIsEmpty(self):
        # act
        
        # assert
        self.assert_(self.table.size() == 0)    
        self.assertEqual(self.table.get("key"), None)
            
    def testIfHashtableIsNotEmpty(self):
        # act
        self.table.put("New", "Map")
        
        # assert
        self.assert_(self.table.size() == 1)        
        
    def testIfEnteredValueIsReturned(self):
        # act
        self.table.put("New", "Map")
        
        # assert
        self.assertEqual(self.table.get("New"), "Map")
        
    def testIfValueIsRewritten(self):
        # act
        self.table.put("New", "Map")
        self.table.put("New", "Map2")

        # assert
        self.assertEqual(self.table.size(), 1)
        self.assertEqual(self.table.get("New"), "Map2")
        
    def testIfRemoveKeyDecreasesSize(self):
        # act
        self.table.put("New", "Map")
        self.table.put("New2", "Map2")

        result = self.table.remove("New2")
        
        # assert
        self.assert_(result)
        self.assertEqual(self.table.size(), 1)
        self.assertEqual(self.table.get("New2"), None)
    
    def testIfFullCollisionModeWorks(self):
        # setup
        table = Hashtable(1)
        
        # act
        table.put("New", "Map")    
        table.put("New1", "Map")    
        table.put("New2", "Map")    
        table.put("New1", "Map2")    
        
        # assert
        self.assertEqual(table.size(),3)
        self.assertEqual(table.get("New1"),"Map2")
       


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
