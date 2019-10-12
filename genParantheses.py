# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:05:17 2019

@author: amaniamr
"""


def genParen(N):
    
    ans = []
    backtrack("",0,0,ans,N)
    print(ans)
    
    

def backtrack(s,left,right,ans,N):
    if len(s) == 2*N:
        ans.append(s)
        return
        
    
    if left < N:
        backtrack(s+"(",left+1,right,ans,N)
    if right < left:
        backtrack(s+")",left,right+1,ans,N)
            
            
genParen(4)