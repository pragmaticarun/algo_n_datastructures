# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 00:17:14 2019

@author: amaniamr
"""

class Trie:
        def __init__(self):
            self.root = {}
            self.end_char = "*"
        
        def addNodes(self,dictionary):
            strings = dictionary.keys()
            for string in strings:
                current = self.root
                for char in string:
                    if char not in current:
                        current[char] = {}
                    current = current[char]
                current[self.end_char] = f"{dictionary[string]} {string}"
            return self.root
        
d = {"i love you":5,
     "i love leetcode":2,
     "ironman":3,
     "V for vendata":4
     }
t = Trie()
t.addNodes(d)

def printTrie(node,result):
    if node is None:
        return
    if "*" in node:
        result.append(node["*"])
    
    for key in node.keys():
        if key != "*":
            printTrie(node[key],result)
            
result = []

def suggest(s):
    x = Trie()
    x.addNodes(d)
    currentNode = x.root
    for char in s:
        if char in currentNode:
            currentNode = currentNode[char]
        else:
            currentNode = None
            break
    suggestions = []
    printTrie(currentNode,suggestions)
    print(suggestions)

printTrie(t.root["i"],result) 
result.sort(key = lambda x: int(x.split(" ",1)[0]))
result = result[::-1] 
print(result)
suggest("i love lee")
        
    
    