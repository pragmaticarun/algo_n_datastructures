# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:29:18 2019

@author: amaniamr
"""

from collections import Counter
def palindromePartitioningMinCuts(string):
    minCuts = minCutPartition(string,0,{})
    
    return minCuts
    
def minCutPartition(string,idx,cache):
    if idx == len(string):
        return -1
    
        
    if idx in cache:
        return cache[idx]
        
    minCuts = float("inf")
    for j in range(idx,len(string)):
        prefix = string[idx:j+1]
        
        if isPalindrome(prefix):
            print(prefix)
            minCutsSuffix = minCutPartition(string,j+1,cache)
            minCuts = min(minCuts,minCutsSuffix+1)
    cache[idx] = minCuts
    
    return minCuts
    
def isPalindrome(string):
    if not string:
        return True
    
    i = 0
    j = len(string) -1
    
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    
    return True
            
    
print(palindromePartitioningMinCuts("abbabbb"))