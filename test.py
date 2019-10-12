# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:28:08 2019

@author: amaniamr
"""

a = [1,2,3,4,5,6,7]

maxSum = float("-inf")

def findNonSeqSum(i,s):
    global maxSum
    s += a[i]
    for j in range(i+2,len(a)):
        findNonSeqSum(j, s)
    if maxSum < s:
        maxSum = s

for i in range(len(a)):
    findNonSeqSum(i,0)
    
print(maxSum)

c = [1,2,3,4,5,4,6,7,8]

def findNonSeqSumIterative(a):
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return a[0]
    maxSum = a[:]
    maxSum[0] = a[0]
    maxSum[1] = max(a[1],a[0])
    
    for i in range(2,len(a)):
        maxSum[i] = max(maxSum[i-1],maxSum[i-2]+a[i])
    
    return maxSum[-1]

print(findNonSeqSumIterative(a))

array = [1,2,3,89,22,44,32,12,1,2,4]

def heapSort(array):
   N = len(array)
   for i in range(N//2,0,-1):
       sink(array,i,N)
   while N > 1:
       swap(array,1,N)
       N -= 1
       sink(array,1,N)
   return array
	
def sink(a,i,N):
	while 2*i <= N:
		j = 2*i
		if j < N and less(a,j,j+1): j += 1
		if not less(a,i,j): break
		swap(a,i,j)
		i = j

def swim(a,i):
	while i > 1:
		j = i // 2
		if less(a,j,i): break
		swap(a,i,j)
		i = j	
	
def less(a,i,j):
	return a[i-1] < a[j-1]
	
def swap(a,i,j):
	a[i-1],a[j-1] = a[j-1],a[i-1]
    
class Heap:
    def __init__(self):
        self.N = 0
        self.a = []
        
    def insert(self,val):
        self.N += 1
        self.a.append(val)
        self.swim(self.N)

    def sink(self,i):
    	while 2*i <=self.N:
    		j = 2*i
    		if j < self.N and self.less(j,j+1): j += 1
    		if not self.less(i,j): break
    		self.swap(i,j)
    		i = j
    
    def swim(self,i):
    	while i > 1:
    		j = i // 2
    		if self.less(i,j): break
    		self.swap(i,j)
    		i = j	
    	
    def less(self,i,j):
    	return self.a[i-1] < self.a[j-1]
    	
    def swap(self,i,j):
    	self.a[i-1],self.a[j-1] = self.a[j-1],self.a[i-1] 
    
    def delMax(self):
        if self.N == 0:
            raise ValueError("No elements in Heap")
        self.swap(1,self.N)
        self.N -= 1
        self.sink(1)
        return self.a.pop()
    
    def sort(self):
       for i in range(self.N//2,0,-1):
           self.sink(i)
       while self.N > 1:
           self.swap(1,self.N)
           self.N -= 1
           self.sink(1)

h = Heap()
h.insert(10)
h.insert(40)
h.insert(2)
print(h.a)
h.sort()
print(h.a)
print(h.delMax())

print(heapSort(array))