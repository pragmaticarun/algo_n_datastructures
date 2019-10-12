# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:50:01 2019

@author: amaniamr
"""


d = {"M":1000,
     "D":500,
     "C":100,
     "L":50,
     "X":10,
     "V":5,
     "I":1,
     "CM":900,
     "CD":400,
     "XC":90,
     "XL":40,
     "IX":9,
     "IV":4,
     }
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
                current[self.end_char] = dictionary[string]
            return self.root
        
def convertToNumber(r):
    t = Trie()
    t.addNodes(d)
    
    num = 0
    current = t.root
    char = ""
    for i in r:
        if i in current:
            current = current[i]
            char = char + i
        else:
            current = t.root
            if i in current:
                current = current[i]
            num += d[char]
            char = i
    num += d[char]
    return num

print(convertToNumber("XVIII"))

    



                    
                
    
    