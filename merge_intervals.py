# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 01:43:45 2019

@author: amaniamr
"""

x = []

x += [1,2]
print(x)

intervals = [[1,2],[1,3]]

for y in intervals:
    x += y
    
print(x)