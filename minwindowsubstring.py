# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:21:13 2019

@author: amaniamr
"""


def minWindow(s,t):
    if not s:
        return ""
    if len(s) == 1:
        if s == t:
            return t
    x = list(t)
    minW = float("inf")
    minWord=""
    i = 0
    a = {}
    while i < len(s):
        if s[i] in x:
            a[s[i]] = i
        if len(a.values()) == len(t):
            idx = a.values()
            print(idx)
            if minW > min(minW,max(idx)-min(idx)):
                minW = min(minW,max(idx)-min(idx))
                minWord = s[min(idx):max(idx)+1]
            i = min(idx)
            a = {}    
        i += 1
            
    return minWord
                    

print(minWindow("bba","bb"))