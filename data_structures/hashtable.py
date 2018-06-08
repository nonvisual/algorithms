'''
Created on May 9, 2018

Implementation of basic Hashtable with indirect addressing
@author: vladimirfux
'''

class Hashtable():
    __size = 0
    
    def __init__(self, address_size=100):
        self.__map = [None] * address_size
        self.__address_size = address_size

        
    def put(self, key, value):
        # compute hashcode
        hashcode = self._hashcode(key)
        result = self._append_or_replace(hashcode, key, value)
        self.__size += result
    
    
    # returns 1 if new entry was added, 0 if it was replaced
    def _append_or_replace(self, hashcode, key, value):
        if(self.__map[hashcode] == None):
            self.__map[hashcode] = []
        bucket = self.__map[hashcode]
        replaced = False
        for i in range(0, len(bucket)):
            if bucket[i][0] == key:
                bucket[i][1] = value
                replaced = True
        if not replaced:
            bucket.append([key, value])
            return 1
        return 0
                
                
    def size(self):
        return self.__size
    
    def get(self, key):
        # compute hashcode
        hashcode = self._hashcode(key)
        bucket = self.__map[hashcode]
        if(bucket == None):
            return None
        
        for i in range(0, len(bucket)):
            if bucket[i][0] == key:
                return bucket[i][1]
        return None
    
    def _hashcode(self, key):
        return hash(key) % self.__address_size

    def remove(self, key):
        hashcode = self._hashcode(key)
        bucket=self.__map[hashcode]
        value = self.get(key)
        if value != None:
            bucket.remove([key,value])
            self.__size-=1
            return True
        return False
            
        
        
