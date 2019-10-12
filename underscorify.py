# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:11:14 2019

@author: amaniamr
"""

def underscorifySubstring(string, substring):
    result = []
    redundant = []
    
    len_s = len(string)
    len_ss = len(substring)
    
    for i in range(len_s):
        if string[i:i+len_ss] == substring:
            result.append(i)
            result.append(i+len_ss)
   
    print(result)
    
    if not result:
        return string
    
    for i in range(2,len(result),2):
        if result[i] <= result[i-1]:
            redundant.append(result[i])
            redundant.append(result[i-1])
    print(redundant)
    
    print(set(result)-set(redundant))
    
    final = ""
    
    for i in range(len(string)):
        if i in result and i not in redundant:
            final += "_"
        final += string[i]
        
    if result[-1] == len(string):
        final += "_"
    
    return final
    
print(underscorifySubstring("this is a test is atestesttest a test","test"))