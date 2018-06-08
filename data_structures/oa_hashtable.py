'''
Created on May 9, 2018
Open addressing hashtable
@author: vladimirfux
'''

class OAHashtable(object):
    '''
    classdocs
    '''
    __size = 0
    
    def __init__(self, address_size, hashcode=None):
        self.__table = [None] * address_size
        self.__address_size = address_size
        if hashcode == None:
            self._hashcode = self._linear_hashcode
        else:
            self._hashcode = hashcode   
            
             
    def put(self, key, value):
        # compute hashcode
        if self.__size >= self.__address_size and self.get(key) == None:
            raise ValueError('The hashtable is full, can not enter a new value and resizing is not supported')        
        
        index = self._get_index(key)
        
        if self.__table[index] == None:
            self.__size += 1
        self.__table[index] = [key, value]

    
    def get(self, key):
        index = self._get_index(key)
        
        if index != None and self.__table[index] != None:
            return self.__table[index][1]
        
        return None
    
    def size(self):
        return self.__size
            
            
    def _linear_hashcode(self, key, count):
        return (hash(key) + count) % self.__address_size
    
    
    def remove(self, key):
        i = self._get_index(key)
        if i != None and self.__table[i] != None :
            self.__table[i] = None
            self.__size -= 1
            return True
        return False
    
    
    ''' Returns first free index, or equal to key'''
    def _get_index(self, key):
        hashcode = self._hashcode(key, 0)
        count = 0
        while self.__table[hashcode] != None  and count < self.__address_size:
            if self.__table[hashcode][0] == key:
                return hashcode
            count += 1
            hashcode = self._hashcode(key, count)
            
        if count == self.__address_size:
            return None
        return hashcode
        
