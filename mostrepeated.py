# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:42:16 2019

@author: amaniamr
"""

class Solution:
    def mostCommonWord(self, paragraph, banned) -> str:
        paragraph = paragraph.lower().replace("!"," ").replace("?"," ").replace("'"," ").replace(","," ").replace(";"," ").replace("."," ").replace("  "," ")
        print(paragraph)
        paragraph = paragraph.strip()
        
        words = paragraph.split(" ")
        words = [x for x in words if x != "" and x not in banned]
        print(words)
        lookup = {}
        max_count = 0
        maxkey = ""
        for word in words:
            if word == "" or word in banned: continue
            print(word)
            if word not in lookup.keys():
                lookup[word] = 0
            lookup[word] += 1
            if lookup[word] > max_count:
                max_count = lookup[word]
                maxkey = word
                
        return maxkey
    
string = "Bob. hIt, baLl"
banned = ["bob", "hit"]

print(Solution().mostCommonWord(string,banned))