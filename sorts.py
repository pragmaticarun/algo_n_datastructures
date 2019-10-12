# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = [4,9,1,-1,3,22,11,18]

for i in range(len(a)):
    for j in range(i,0,-1):
        if a[j] < a[j-1]:
            a[j-1],a[j] = a[j],a[j-1]
        else:
            break
        
#print(a)

b = [90,75,42,1,3,22,27,65,41,0,-1]
h = 0
while(h < len(b)/3): h = 3*h + 1

while h>=1:
    for i in range(h,len(b)):
        j = i
        while j >= h and b[j] < b[j-h]:
            b[j-h],b[j] = b[j],b[j-h]
            j -= h
    h = h//3

#print(b)
a = [4,9,1,-1,3,22,11,18]   
def merge(a,aux,lo,mid,hi):
  for k in range(lo,hi+1):
    aux[k]=a[k]
  i = lo
  j = mid+1
  for k in range(lo,hi+1):
    if j > hi: 
      a[k] = aux[i]
      i += 1
    elif i > mid:
      a[k] = aux[j]
      j += 1
    else:
      if aux[i] > aux[j]:
        a[k] = aux[j]
        j += 1
      else:
        a[k] = aux[i]
        i += 1
     
        
def merge_helper(a):
    aux = a.copy()
    sz=1
    while sz < len(a):
        print(sz)
        j = 0
        for j in range(0,len(a)-sz,sz+sz):
            print(j,j+sz-1,min(j+sz+sz-1,len(a)-1))
            merge(a,aux,j,j+sz-1,min(j+sz+sz-1,len(a)-1))
        sz += sz
merge_helper(b)     
print(f"Merge Result {b}")

a = [4,9,1,-1,3,22,11,18]
def partition(a,lo,hi):
    i = lo+1
    j = hi
    v = a[lo]
    while i <= j:
        while i <= hi and v > a[i]:
            i += 1
        while j >= lo and v < a[j]:
            j -= 1
        if i < j:
            a[i],a[j] = a[j],a[i]
    a[lo],a[j] = a[j],a[lo]
    
    return j

def select(a,k):
    k = k-1
    lo = 0
    hi = len(a)-1
    while lo <= hi:
        j = partition(a,lo,hi)
        if j > k:
            hi = j - 1
        elif j < k:
            lo = j + 1
        else:
            print(a[j])
            break
b = [90,75,42,1,3,22,27,65,41,0,-1]
#select(b,1)
#select(b,len(b))
    


#partition(a,0,len(a)-1)

def three_way_quick_sort(a,lo,hi):
    if lo >= hi:
        return
    v = a[lo]
    i = lo
    lt = lo
    gt=hi

    while i <= gt:
        if v > a[i]:
            a[i],a[lt] = a[lt],a[i]
            i += 1
            lt += 1
        elif v < a[i]:
            a[i],a[gt] = a[gt],a[i]
            gt -= 1
        else:
            i += 1
    
    three_way_quick_sort(a,lo,lt-1)
    three_way_quick_sort(a,gt+1,hi)

three_way_quick_sort(b,0,len(b)-1)
print(f"Merge result Quick sort three way {b}")
        