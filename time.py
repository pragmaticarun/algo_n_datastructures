# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 23:25:02 2019

@author: Arunkumar Maniam Rajan
"""

prefix_sum = [0] * 11 #Assume time range from 0 to 10

#Assume these are intervals
call_start_end = [[2,3],[0,1],[2,4],[5,6],[0,10]] #start,end

query = [0,4]  #[start,end]
#Excludes the call that ended at interval end.
#if needs including we can change a[x[1]+1] -= 1
for time in call_start_end:
    start = time[0]
    end = time[1]
    prefix_sum[start] += 1
    prefix_sum[end] -= 1
    

for i in range(1,len(prefix_sum)):
    prefix_sum[i] = prefix_sum[i-1] + prefix_sum[i]
    
# number calls between 0 and 4 active essentially means the calls that are
# active at time 4 with the prefix sum array. 

print(prefix_sum[4])
#prefix_sum = [2, 1, 3, 2, 1, 2, 1, 1, 1, 1, 0] 

