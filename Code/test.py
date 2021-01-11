'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-01-10 11:18:07
'''
import collections    
import heapq
from collections import deque
import functools
# from numba import njit
import numpy as np
import bisect

def function(nums):
    if not nums:
        return []
    n = len(nums)
    if n ==1 :
        return [str(nums[0])]
    ans = []
    i = 0
    while i<n:
        j = i+1  

        while j<n and nums[j]-nums[j-1] == 1:
            j += 1
            
        if j-1 == i:
            ans.append('%d'%(nums[i]))
        else:
            ans.append('%d->%d'%(nums[i],nums[j-1]))
        i = j
    return ans        
   
something = function(nums = [0,1,2,4,5,7])
print(something)