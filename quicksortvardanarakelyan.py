# -*- coding: utf-8 -*-
"""quickSortVardanArakelyan.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MhPnIEkN8BREphIabUI_TpOTHAXTukaS
"""

def partition(arr, l,r):
  pivot = arr[(l+r)//2]
  i = l
  j = r
  while(i <= j):
    while(arr[i] < pivot ):
      i +=1
    while(arr[j] > pivot):
      j-=1
    if(i >= j):
      break
    arr[i], arr[j] = arr[j], arr[i]
    i+=1
    j-=1
  return j

def quickSort(arr,l,r):
  if l<r:
    q = partition(arr,l,r)
    quickSort(arr,l,q)
    quickSort(arr,q+1,r)

arr = [9,-7,8,5,6,-4.3,55,43,65,4.7,-675]
quickSort(arr,0,len(arr)-1)
print(arr)