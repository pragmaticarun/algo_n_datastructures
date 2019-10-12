# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 08:23:30 2019

@author: amaniamr
"""

class Board:
    def __init__(self,N):
        self.N = N
        self.col = [0 for _ in range(N)]
        self.btt = [0 for _ in range(2*N)]
        self.ttb = [0 for _ in range(2*N)]
        self.queens = set()
        self.ans = []
        
    def placeQueen(self,row,col):
        self.col[col] = 1
        self.btt[row+col] = 1
        self.ttb[row-col] = 1
        self.queens.add((row,col))
        
    def canPlace(self,row,col):
        return not (self.col[col] + self.btt[row+col] + self.ttb[row-col])
    
    def removeQueen(self,row,col):
        self.col[col] = 0
        self.btt[row+col] = 0
        self.ttb[row-col] = 0
        self.queens.remove((row,col))
        
    def solve(self):
        self.tryPosition(0)
        return self.ans
                
    def tryPosition(self,row):
        for col in range(self.N):    
            if self.canPlace(row,col):
                self.placeQueen(row,col)
                if row + 1 == self.N:
                    self.ans.append(self.queens.copy())
                else:
                    self.tryPosition(row+1)
                self.removeQueen(row,col)
                
                
print(Board(4).solve())
                


        
    