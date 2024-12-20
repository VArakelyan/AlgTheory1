# -*- coding: utf-8 -*-
"""Search algorithms

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ls1wk5zxjlSMP1wjLjY3BLB5w9mzvCkN
"""

# linear search

def lin_search(a, key):
  for i in a:
    if i == key:
      return True
  return -1

a = [1,2,3,4,5,6,7]
key = 11
lin_search(a,key)

# binary search

def bin_search(a,low,high,key):
  mid = (low+high)//2
  if low <= high:
    if a[mid] == key:
      print(mid)
    elif key < a[mid]:
      bin_search(a,low,mid-1,key)
    elif a[mid] < key:
      bin_search(a,mid+1,high,key)
  if low > high:
    print(False)
a = [1,2,3,4,5,6,7,8]
key = 1
bin_search(a,0,len(a)-1,key)

# ternary search

def ter_search(a,low,high,key):
  mid1 = low + (high - low)//3
  mid2 = high - (high - low)//3

  if high >= low:

    if a[mid1] == key or a[mid2] == key:
      print(True)

    if a[mid1] < key < a[mid2]:
      ter_search(a,mid1+1,mid2-1,key)

    if key > a[mid2]:
      ter_search(a,mid2+1,high,key)

    if key < a[mid1]:
      ter_search(a,low,mid1-1,key)
  else:
    print(False)

a = [1,2,3,4,5,6,7,8]
key = 10
ter_search(a,0,len(a)-1,key)

import math
# jump search
def jump_search(a,target):
  prev = 0
  n = len(a)
  step = int(math.sqrt(n))

  while a[min(step, len(a)) - 1] < target:
    prev = step
    step += int(math.sqrt(n))
    if prev >= n:
      return -1

  for i in range(prev, min(step, len(a))):
    if a[i] == target:
      return i

a = [1,2,3,4,5,6,7,8]
key = 7
jump_search(a,key)

#interpolation search
import math
def interpol(a, high, low,key):


  if low <= high and key >= a[low] and key <= a[high]:
    if a[high] == a[low]:
            if a[low] == key:
                return low


    pos = (low + (((key - a[low]) * (high - low)) // (a[high] - a[low])))
    if a[pos] > key:
      return interpol(a,pos-1,low, key)
    elif a[pos] < key:
      return interpol(a,high,pos+1,key)

    if a[pos] == key:
      return pos

  return -1

a = [10,12,13,16,18,19,20,21,22,23,24,33,35,42,47,47]
key = 23
high = len(a) - 1
low = 0
interpol(a,high,low,key)

# Exponential search

def expon_search(a,key):
  n = len(a)
  if a[0] == key:
    return 0

  i = 1
  while i < n and a[i] <= key:
    i *= 2

  return bin_search(a, i//2, min(i,n),key)


a = [10,12,13,16,18,19,20,21,22,23,24,33,35,42,47,47]
key = 13
expon_search(a,key)

