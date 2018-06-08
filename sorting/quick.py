'''
Created on Apr 18, 2018

@author: vladimirfux
'''
from random import randint

class QuickSort(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''

    
    @staticmethod
    def sort(array, i, j):    
        if(i<j):
            k = randint(i, j)
            pivot = QuickSort.pivot(array, i,j,k)
            QuickSort.sort(array,i,pivot-1)
            QuickSort.sort(array,pivot,j)
    
    @staticmethod
    def switch(array,i,j):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp 
        
    '''
    for the subarray i-j and i<=k<=j it puts 
    all elements below [k] before [k] and above [k] after [k]
    '''
    @staticmethod
    def pivot(array,i,j,k):
        if(k>j or k<i or i>j):
            print("k is outside the array or i>j")
            return -1
        
        #switch k with the last element
        pivot = array[k]
        QuickSort.switch(array,j,k)
        
        left = -1
        right = j 
        while left<right:
            left+=1
            if(array[left]>pivot):
                while array[right]>=pivot and right>left:
                    right-=1
                #switch left and right
                if(left<right):
                    QuickSort.switch(array,left,right)
                else:
                    QuickSort.switch(array,j,right)        
    
        return right            
        
        
        
        