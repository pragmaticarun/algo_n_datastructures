# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 05:36:50 2019

@author: atara
"""
import collections
def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()

print(groupAnagrams(["eat","ate"]))