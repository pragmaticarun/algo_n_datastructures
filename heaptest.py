# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 08:45:18 2019

@author: amaniamr
"""

class Heap:
    def __init__(self,comp = "MIN"):
        self.N = 0
        self.backing_array = []
        if comp == "MIN":
            self.compareFunction = self.less
        else:
            self.compareFunction = self.greater
        
    def insert(self,value):
        self.backing_array.append(value)
        self.N += 1
        self.swim(self.N)
    
    def remove(self):
        self.swap(1,self.N)
        self.N -= 1
        val = self.backing_array.pop()
        self.sink(1)
        return val
        
    def sink(self,node):
        child = 2*node
        
        while child <=self.N:
            if child < self.N and not self.compareFunction(child,child+1):
                child = child + 1
            if self.compareFunction(node,child):
                break
            self.swap(node,child)
            node = child
            child = 2* node
        
    def swim(self,node):
        root = node // 2
        while root >= 1:
            if  not self.compareFunction(root,node):
                self.swap(node,root)
                node = root
                root = node // 2
            else:
                break
                
    def peek(self):
        if self.N:
            return self.backing_array[0]
        else:
            return -1
        
    def swap(self,i,j):
        self.backing_array[i-1],self.backing_array[j-1] = self.backing_array[j-1],self.backing_array[i-1]
        
    def less(self,i,j):
        return self.backing_array[i-1] < self.backing_array[j-1]
    
    def greater(self,i,j):
         return self.backing_array[i-1] > self.backing_array[j-1]   
         

h = Heap("MIN")
h.insert(10)
h.insert(20)
h.insert(45)
h.insert(50)
h.insert(5)
print(h.remove())
print(h.remove())
print(h.remove())
print(h.remove())
print(h.remove())
print(h.peek())
    
                