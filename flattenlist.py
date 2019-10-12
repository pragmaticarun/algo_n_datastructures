# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:24:29 2019

@author: amaniamr
"""

a = [1,[2,3,[5],6],7]

def flatten(a):
    if type(a) == list:
        for x in a:
            flatten(x)
    else:
        print(a)
        
flatten(a)