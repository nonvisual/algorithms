'''
Created on Apr 18, 2018

@author: vladimirfux
'''
from math import floor
class MergeSort(object):
    
    @staticmethod
    def sort(array, i, j):
        if(i < j):
            k = (int)(i + floor((j - i) / 2))
            MergeSort.sort(array, i , k)
            MergeSort.sort(array, k + 1, j)
            MergeSort.merge(array, i, j, k)
            
            
            
       
    
    @staticmethod
    def merge(array, i, j, k):
        temp = [None] * (j - i + 1)
        left = i
        right = k + 1
        index = 0
        while(index < (j - i + 1)):
            if(right > j or (left <= k and array[left] < array[right])):
                temp[index] = array[left]
                left += 1
            else:
                temp[index] = array[right]
                right += 1
            index += 1
               
        for l in range(i, j+1):
            array[l] = temp[l-i]
            
