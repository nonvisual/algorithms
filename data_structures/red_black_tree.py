'''
Created on Apr 10, 2018
Properties of red-black tree

1. Every node is either red or black.
2. The root is black.
3. Every leaf (NIL) is black.
4. If a node is red, then both its children are black.
5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.

@author: vladimirfux
'''

from enum import Enum
from data_structures.binary_search_tree import BinaryTree 
from platform import node
class Color(Enum):
    RED = 1
    BLACK = 2
    
class ColoredNode(object):
    '''
    classdocs
    '''
    def __init__(self, parent, left_child, right_child, key, value, color):
        '''
        Constructor
        '''
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.key = key
        self.value = value
        self.color = color
        
        
class RedBlackTree(BinaryTree):
    
    
    def __init__(self):
        self.root = None
        
    
    # override     
    def insert(self, key, value): 
        
        if(key != None):
            if(self.root == None):
                self.root = ColoredNode(None, None, None, key, value, Color.RED)
                node = self.root
            else:
                x = self.root
                y = None
                while(x != None):
                    if(key <= x.key):
                        y = x
                        x = x.left_child
                    else:
                        y = x
                        x = x.right_child
                node = ColoredNode(y, None, None, key, value, Color.RED)
                if(y == None):
                    self.root = node
                elif(key <= y.key):
                    y.left_child = node
                else:
                    y.right_child = node
        
        self.__fix_insert_rb(node)
    
    
    def __fix_insert_rb(self, z):
        while z.parent != None and z.parent.color == Color.RED:
            if z.parent == z.parent.parent.left_child:
                y = z.parent.parent.right_child
                if y != None and  y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                elif z == z.parent.right_child:
                    z = z.parent
                    self.__left_rotate(z)
                else:    
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.__right_rotate(z.parent.parent)
            # symmetric for left uncle
            else:
                y = z.parent.parent.left_child
                if y != None and y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                elif z == z.parent.left_child:
                    z = z.parent
                    self.__right_rotate(z)
                else:
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.__left_rotate(z.parent.parent)
                    
        self.root.color = Color.BLACK            
    
    # override
    def delete(self, key):
        pass
    
    def __left_rotate(self, x):
        y = x.right_child
        x.right_child = y.left_child
        if y.left_child != None:
            y.left_child.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left_child:
            x.parent.left_child = y
        else: x.parent.right_child = y
        y.left_child = x
        x.parent = y
    
       
    def __right_rotate(self, y):
        x = y.left_child
        
        # right child of x -> left child of y
        y.left_child = x.right_child
        if x.right_child!=None:
            x.right_child.parent = y 
        
        # fix parent of x
        if y.parent == None:
            self.root = x 
        elif y == y.parent.left_child:
            y.parent.left_child =x 
        else:
            y.parent.right_child = x 
        x.parent = y.parent
                 
        y.parent = x 
        x.right_child = y 
        
       
        
        
    def print_in_order(self):
        self.__print_in_order(self.root)
    
    def __print_in_order(self, node):
        if(node != None):
            self.__print_in_order(node.left_child)
            print(str(node.key) + "=" + ("R" if node.color == Color.RED else"B") + ", ")
            self.__print_in_order(node.right_child)
    ''' fixing red black properties, while loop maintains 
    a. Node  ́ is red.
    b. If  ́:p is the root, then  ́:p is black.
    c. If the tree violates any of the red-black properties,
    then it violates at most one of them, and the violation is 
    of either property 2 or property 4. If the tree violates property 2,
    it is because  ́ is the root and is red. If the tree violates property 4,
    it is because both  ́ and  ́:p are red.'''
