# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:11:22 2019

@author: atara
"""

a = [1,49,11,2,3,4,5,6,7,8,9,10,13]

def largestRange(array):
    if len(array) < 1:
        return []
    elif len(array) == 1:
        return [array[0],array[0]]
        
    array.sort()
    hi = 1
    maxlen = float("-inf")
    maxrange = []
    start = 0
    while hi < len(array):
        if array[hi] != array[hi-1]+1 and array[hi] != array[hi-1]:
            if hi - start > maxlen:
                maxlen = hi - start
                maxrange = [array[start],array[hi-1]]
            start = hi
            hi = hi + 1
        else:
            hi = hi + 1
    if hi - start > maxlen:
        maxlen = hi - start
        maxrange = [array[start],array[hi-1]]
        
    return maxrange

print(largestRange(a))