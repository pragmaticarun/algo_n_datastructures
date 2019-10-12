# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:27:42 2019

@author: amaniamr
"""

from collections import defaultdict

def findLadders(beginWord: str, endWord: str, wordList):
    if not beginWord or not wordList  or endWord not in wordList or beginWord == endWord: 
        return []

    #Create intermediateState dictionary

    d = defaultdict(list)
    visited = {}
    result = []
    for word in wordList:
        L = len(word)
        for i in range(L):
            intermediate_word = word[:i] + "*" + word[i+1:]
            d[intermediate_word].append(word)
    visited = {}
    queue = [(beginWord,[beginWord])]
    visited[beginWord] = True
    while(queue):
        currentWord,l = queue.pop(0)
        L = len(currentWord)
        visited[currentWord] = True
        for i in range(L):
            intermediate_word = currentWord[:i] + "*" + currentWord[i+1:]

            for word in d[intermediate_word]:
                if word == endWord:
                    l.append(word)
                    result.append(l)
                if word != endWord and word not in visited:
                    x = l[:]
                    x.append(word)
                    queue.append((word,x)) 
                    

    result.sort(key = len)
    newresult = []
    if result:
        smallest = len(result[0])
        
        for l in result:
            if len(l) == smallest:
                newresult.append(l)
            else:
                break

    return newresult

print(findLadders("hit","cog",["hot","dot","dog","lot","log","cog"]))