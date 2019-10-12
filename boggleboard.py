# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:30:53 2019

@author: amaniamr
"""

class Solution:
    def exist(self, board, word) -> bool:
        visited = [[False for letter in row] for row in board]
        lookup = Trie()
        lookup.insertWord(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if(explore(board,i,j,lookup.root,visited)):
                    return True
        return False
    
def explore(board,i,j,currentNode,visited):
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return False
        
    if visited[i][j]:
        return False
    
    letter = board[i][j]
    if letter in currentNode:
        visited[i][j] = True
        if "*" in currentNode[letter]:
            return True
        neighbours = getNeighbours(i,j)
        for n in neighbours:
            if(explore(board,n[0],n[1],currentNode[letter],visited)):
                return True
            
        visited[i][j] = False
    return False

class Trie:
    def __init__(self):
        self.root = {}
        self.endChar = "*"
    
    def insertWord(self,word):
        currentNode = self.root
        for letter in word:
            if letter not in currentNode:
                currentNode[letter] = {}
            currentNode = currentNode[letter]
        currentNode[self.endChar] = word

def getNeighbours(i,j):
    neighbours = []
    neighbours.append([i-1,j-1])
    neighbours.append([i-1,j])
    neighbours.append([i-1,j+1])
    neighbours.append([i, j-1])
    neighbours.append([i,j+1])
    neighbours.append([i+1,j+1])
    neighbours.append([i+1,j-1])
    neighbours.append([i+1,j])
    
    return neighbours
