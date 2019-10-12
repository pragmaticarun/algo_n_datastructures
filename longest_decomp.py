# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:52:54 2019

@author: amaniamr
"""

def longestDecomposition(text: str) -> int:
    
    def maxk(text,start_idx,end_idx,cache):
        if start_idx >= end_idx:
            return -1
        x = tuple((start_idx,end_idx))
        if x in cache:
            return cache[x]
        maxk_val = float("-inf")
        for j in range(start_idx,end_idx+1):
            prefix = text[start_idx:j+1]
            match_suffix = text[end_idx - (j-start_idx):end_idx+1]
            
            if prefix == match_suffix:
                print("prefix " + prefix)
                print("match_suffix " + match_suffix)
                suffixlen = maxk(text,j+1,end_idx - (j-start_idx)-1,cache)
                print(suffixlen)
                maxk_val = max(maxk_val,suffixlen+2)
        cache[x] = maxk_val
        
        return maxk_val
        
    return maxk(text,0,len(text)-1,{})


print(longestDecomposition("antaprezatepzapreanta"))