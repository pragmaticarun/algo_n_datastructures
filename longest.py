# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:21:52 2019

@author: amaniamr
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = float("-inf")
        a = {}
        i = 0
        while i < len(s):
            print(a.items())
            print(a.keys())
            if a and (s[i] in a.keys()):
                if maxlen < len(a.keys()):
                    maxlen = len(a.keys())
                i = a[s[i]]+1
                if i >= len(s):
                    break
                a = {}
                a[s[i]] = i
                i += 1
            else:
                a[s[i]] = i
                i += 1
        if a and maxlen < len(a.keys()):
            maxlen = len(a.keys())      
            
        return maxlen
    
    
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))