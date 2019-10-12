# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:35:51 2019

@author: amaniamr
"""
nums = [1,2,4,8,16,32,64,128]
target = 96
def threeSumClosest(nums, target):
    nums.sort()
    smallest = float("inf")
    val = 0
    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            total = (nums[i]+nums[j]+nums[k])
            if abs(target - total) < smallest:
                smallest = abs(target - total)
                val = total
            if target == total:
                return total
            elif total < target:
                j = j + 1
            else:
                k = k - 1

    return val

print(threeSumClosest(nums,target))