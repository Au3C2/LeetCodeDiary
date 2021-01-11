'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-01-08 10:50:05
'''
import collections    
import heapq
from collections import deque
import functools
# from numba import njit
import numpy as np
import bisect

def function(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:]+nums[:-k]
    return nums
something = function([1,2],3)
print(something)