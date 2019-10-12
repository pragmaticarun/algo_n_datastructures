# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:12:57 2019

@author: atara
"""

def fourNumberSum(array, targetSum):
    array.sort()
    result = []
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            k = j + 1
            h = len(array) - 1
            while k < h:
                currentSum = array[i] + array[j] + array[k] + array[h]
                print(i,j,k,h,currentSum)
                if targetSum < currentSum:
                    h -= 1
                elif targetSum > currentSum:
                    k += 1
                else:
                    result.append([array[i],array[j],array[k],array[h]])
                    k += 1
                    h -= 1
    return result

#print(fourNumberSum([1,2,3,4,5,6,7],10))


        
def powersetHelper(array,idx):
    if idx < 0:
        return [[]]
    
    val = array[idx]
    subsets= powersetHelper(array,idx-1)
    for i in range(len(subsets)):
        s = subsets[i]
        subsets.append(s + [val])
    return subsets
    
def powerset(array):
    return powersetHelper(array,len(array)-1)
    
        

                
            
    return result
print(powerset([1,2,3]))