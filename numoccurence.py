# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 08:02:26 2019

@author: atara
"""

from collections import Counter,defaultdict

a = [-3,0,0,-3,1,1,1,-3,10,0]

c = Counter(a)
g = defaultdict(list)
for items in c.items():
    g[items[1]].append(items[0])
    if len(g[items[1]]) > 1:
        print("False")
    
print("True")
    

def removeDuplicates(s: str, k: int) -> str:
    if not s:
        return s
    
    if len(s) == 1 and k == 1:
        return ""
    
    stack = []
    count_stack = []
    count = 0
    for char in s:
        if stack and stack[-1] == char:
            if count + 1== k:
                while count:
                    stack.pop()
                    count_stack.pop()
                    count = count -1
                
                if count_stack:
                    count = count_stack[-1]
                else:
                    count = 0
            else:
                count += 1
                stack.append(char)
                count_stack.append(count)
            
        else:
            count = 1
            if k != count:
                stack.append(char)
                count_stack.append(count)
            
    print(stack)
    print(count_stack)
    
removeDuplicates("deeedbbcccbdaa",3)
s = "abc"
t = "bcde"

costs = [abs(ord(a)-ord(b)) for a,b in zip(s,t)]
print(costs)
                