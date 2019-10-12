# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:11:32 2019

@author: atara
"""

a = [1,2,3]
result = []
def perm(a,i):
    if i == len(a):
        result.append(a[:])
        return
        
    for j in range(i,len(a)):
        a[i],a[j] = a[j],a[i]
        perm(a,i+1)
        a[i],a[j] = a[j],a[i]
    
perm(a,0)
print(result)
        
    