# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 00:20:22 2019

@author: atara
"""
a = [
     [1,3,4,10],
     [2,5,9,11],
     [6,8,12,15],
     [7,13,14,16]]
def zigzagTraverse(array):
    i = 0
    j = 0
    direction = 1
    coefx = 1
    coefy = -1
    ly = 0
    lx = 0
    hx = len(array)
    hy = len(array[0])
    result = []
    total = 0
    result.append(array[i][j])
    swap_coef = False
    while True:
        i += coefx * direction
        j += coefy * direction 
        if i >= len(array) or j < ly or j >= hy or i < lx:
            direction = direction  * (-1)
            if i >= hx:
                i = hx -1
            if j <ly :
                j = ly
            if j >= hy:
                j = hy -1
                swap_coef = True
            if i < lx:
                i = lx
        result.append(array[i][j])
        print(i,j,direction)
        if j == hy-1:
            break
    direction = 1
    coefx = -1
    coefx = 1
    while total < hx * hy:    
        total += 1
        i += coefx * direction
        j += coefy * direction
        if i >= len(array) or j < ly or j >= hy or i < lx:
            direction = direction * -1
            if i >= hx:
                i = hx -1
                coefy = -coefy
            if j <ly :
                j = ly
            if j >= hy:
                j = hy -1
                coefx = -coefx
            if i < lx:
                i = lx
        result.append(array[i][j])
        print(i,j,direction)
        if hx-1 == i and hy-1 == j:
            break
        
    return result

print(zigzagTraverse(a))