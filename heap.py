# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 09:21:39 2019

@author: Arunkumar Maniam Rajan
"""
a = [1,2,3,4,5,0,8,9,11,12,45]

def swap(a,i,j):
    a[i-1],a[j-1] = a[j-1],a[i-1]

def minprop(a,i,j):
    return a[i-1] < a[j-1]

def maxprop(a,i,j):
    return a[i-1] > a[j-1]

def parent(i):
    return i // 2

def leftChild(i):
    return 2*i

def rightChild(i):
    return 2*i + 1

def swim(a,i,comp):
    j = i // 2
    while j >= 1 and comp(a,i,j): 
        swap(a,i,j)
        i = j
        j = i // 2
    
def sink (a,i,N,comp):
    j = 2*i
    while j <= N:
        if j < N and not comp(a,j,j+1) : j += 1
        if not comp(a,i,j):
            swap(a,i,j)
        else:
            break
        i = j
        j = 2*i
        
   
def heapify(a,comp):
    N = 0
    b = []
    for i in range(len(a)):
        N += 1
        b.append(a[i])
        swim(b,N,comp)
    return b

def heapifyInplace(a,comp):
    for i in range(len(a)//2,0,-1):
        sink(a,i,len(a),comp) 
    
    

heapify(a,maxprop)
    
#c = heapify(a,maxprop)

print(a)
def doSort(c,comp):
    N = len(c)
    for i in range(N,0,-1):
        swap(c,1,i)
        sink(c,1,i-1,comp)
        

def extract(a,invariant):
    if len(a) == 0 : return None
    
    swap(a,1,len(a))
    x = a.pop()
    sink(a,1,invariant)
    print(x)
    print(a)
    
def heapSort(a):
    if a is None: return
    heapifyInplace(a,maxprop)
    doSort(a,maxprop)
    
heapSort(a)
print(a)
    
