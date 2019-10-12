# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:00:51 2019

@author: amaniamr
"""

#!/bin/python3


import os


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    x = [0 for _ in range(n)]
    for q in queries:
        for j in range(q[0],q[1]+1):
            x[j-1] += q[2]
    return max(x)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
