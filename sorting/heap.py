'''
Created on May 7, 2018

@author: vladimirfux
'''
import math as mt

def sort(array):
    pass

def heapify(array, i):
    largest = None
    if left(array, i) != None and left(array, i) > array[i]:
        largest = 2*i + 1
    if right(array, i) != None and right(array, i) > array[i]:
        largest = 2*(i+1)
        
    if largest != None:
        _switch(array, i, largest)    
        heapify(array, largest)    


def build_heap(array):
    l = len(array)
    for i in range(l / 2, -1, -1):
        heapify(array, i)
    
    
def left(array, i):
    if 2 * (i) + 1 >= len(array):
        return None
    else:
        return array[2 * (i) + 1]

def right(array, i):
    if 2 * (i + 1) >= len(array):
        return None
    else:
        return array[2 * (i + 1)]

def parent(array, i):
    if(i == 0):
        return None
    index = int(mt.ceil(i / 2))
    return array[index]

def _switch(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    
def is_heap(array):
    for i in range(0, int(len(array) / 2) + 1):
        if left(array, i) != None and array[i] < left(array, i):
            return False
        if right(array, i) != None and array[i] < right(array, i):
            return False
    return True    

