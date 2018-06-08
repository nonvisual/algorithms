'''
Created on Apr 10, 2018

@author: vladimirfux
'''
from platform import node
from logging import root

class Node:
    '''
    classdocs
    '''
    def __init__(self, parent, left_child, right_child, key, value):
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.key = key
        self.value = value
        

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key, value): 
        if(key != None):
            if(self.root == None):
                self.root = Node(None, None, None, key, value)
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
                node = Node(y, None, None, key, value)
                if(y == None):
                    self.root = node
                elif(key <= y.key):
                    y.left_child = node
                else:
                    y.right_child = node
                    

    
    def search(self, key):
        if(self.root == None or key == None):
            return None
        x = self.root
        while(x != None):
            if(key == x.key):
                return x
            elif(key <= x.key):
                x = x.left_child
            else:
                x = x.right_child
        return None
        
    def print_in_order(self):
        self.__print_in_order(self.root)
    
    def __print_in_order(self, node):
        if(node != None):
            self.__print_in_order(node.left_child)
            print(node.key)
            self.__print_in_order(node.right_child)

    
    
    
    
    
    def ordered_values(self):
        return self.__ordered_values(self.root)
    
    def __ordered_values(self, node):
        if node != None:
            a = []
            a += self.__ordered_values(node.left_child)
            a.append(node.value)
            a += self.__ordered_values(node.right_child)
            return a
        return []
    
    def ordered(self):
        return self.__ordered(self.root)
    
    def __ordered(self, node):
        if node != None:
            a = []
            a += self.__ordered(node.left_child)
            a.append(node)
            a += self.__ordered(node.right_child)
            return a
        return []
    
    def min(self, node):
        if node != None and node.left_child != None:
            return self.min(node.left_child)
        return node
     
    def max(self, node):
        if node != None and node.right_child != None:
            return self.min(node.right_child)
        return node       
    
    
    
    
    
    def successor(self, node):
        if node == None:
            return None
        if node.right_child != None:
            return self.min(node.right_child)
        y = node
        x = node.parent
        while x != None and y == x.right_child:
            y = x
            x = x.parent
           
        return x
        
    def successorByKey(self, key):
        return self.successor(self.search(key))               
           
           
    def predcessor(self, node):
        if node == None:
            return None
        if node.left_child != None:
            return self.max(node.left_child)
        y = node
        x = node.parent
        while x != None and y == x.left_child:
            y = x
            x = x.parent
           
        return x
        
    def predcessorByKey(self, key):
        return self.predcessor(self.search(key))        
            
    '''
        Moves a tree v to be the child of u's parent instead of u
    '''
    def transplant(self, u, v):
        if(u == None):
            self.root = v
        elif u.parent.left_child==u:
            u.parent.left_child=v
        else:
            u.parent.right_child=v
        if v!=None:
            v.parent = u.parent
             
                
        
    '''
    4 cases: 1) 
    '''
            
    def delete(self, key):
        node = self.search(key)
        if node == None:
            return False
        if node.left_child == None:
            self.transplant(node, node.right_child)
        elif node.right_child == None:
            self.transplant(node, node.left_child)
        else:
            y = self.successor(node)
            if y != node.right_child:
                self.transplant(y, y.right_child)
                y.right_child = node.right_child
                y.right_child.parent = y
            
            self.transplant(node, y)
            y.left_child = node.left_child
            y.left_child.parent = y                
            
        return True
