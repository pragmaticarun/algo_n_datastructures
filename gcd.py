# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 06:44:27 2019

@author: atara
"""

def gcd(x,y):
    if x == 0 or y == 0:
        return x if y == 0 else y
    x = x % y
    return gcd(y,x)

def gcd_iterative(x,y):
    while(y != 0):
        z = x % y
        x = y
        y = z
    return x

def gcd_euclid(x,y):
    #GCD(x,y) = GCD(x,x) = x
    while(x != y):
        if x > y:
            x = x-y
        else:
            y = y -x
    return x

print(gcd_euclid(420,96))