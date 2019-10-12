# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:16:31 2019

@author: amaniamr
"""

a = [1,2,3,4]
def perm(a):
    ans = []
    permHelper(a,0,ans)
    print(ans)
        
def permHelper(a,i,ans):
    if i == len(a):
        ans.append(a[:])
        return 
    
    for j in range(i,len(a)):
        a[i],a[j] = a[j],a[i]
        permHelper(a,i+1,ans)
        a[i],a[j] = a[j],a[i]
        
        
perm(a)

def perm2(a):
        subset = [[]]
        for i in range(len(a)):
            for sub in subset:
                subset += sub.append(a[i])
        return subset
    

print(perm2(a))
        
    
    
        