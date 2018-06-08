'''
Created on Apr 26, 2018


Uses counting sort as stable sorting
@author: vladimirfux
'''
import numpy as np
import counting as cn


def sort(array, max_digits):
    sortedList = array[:]
    for i in range(1, max_digits + 1):
        sortedList = sort_by_digit(sortedList, i)
    return sortedList




def sort_by_digit(array, digitNumber):
    digits = []
    for i in range(0, len(array)):
        digits.append(get_digit(array[i], digitNumber))
    strc = zip(digits, array)
    sortedList = cn.sort(strc, 9, key=lambda x: x[0])
    
    
    return list(zip(*sortedList)[1])              
        
        
def get_digit(num, digit):
    return num // 10 ** (digit - 1) - (num // 10 ** digit) * 10 
    
