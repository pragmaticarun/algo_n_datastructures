# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:35:58 2019

@author: amaniamr
"""


def wordBreak(s, wordDict):
    return checkPrefix(s,wordDict,0)


def checkPrefix(s,wordDict,idx):
    if idx == len(s):
        return True
    
    for i in range(idx,len(s)):
        if s[idx:i+1] in wordDict and checkPrefix(s,wordDict,i+1):
            return True
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
        
#print(wordBreak("leet",["leet","abbaa"]))

pattern = "yxxxx"
pattern = ["y" for j in pattern if j == "x"]
#print(pattern)


def multiStringSearch(bigString, smallStrings):
    inputString = bigString.split()
    
    x = [ss in inputString for ss in smallStrings]
    
    return x

print(multiStringSearch("shopping",["shop"]))