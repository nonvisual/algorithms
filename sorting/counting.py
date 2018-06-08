'''
Created on Apr 26, 2018
Counting sort implementation
@author: vladimirfux
'''


def sort (array, n, key=None):
    count_array = [0] * (n + 1)  # size n + zero
    s = len(array)
    sorted_array = [-1] * s  # size of array

    if(key == None):
        key = lambda x: x
    # count all occurencies 
    for i in range(0, s):
        if(key(array[i]) > n):
            raise ValueError("Max value is wrong, array contains higher values")
        count_array[key(array[i]) ] += 1
    
    # count elements below current
    for i in range(1, n + 1):
        count_array[i] += count_array[i - 1]
        
    # insert values
    for i in range(s - 1, -1, -1):
        sorted_array[count_array[key(array[i])] - 1] = array[i]
        count_array[key(array[i])] -= 1
                
    return sorted_array
