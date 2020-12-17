'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2020-12-16 17:26:11
'''
import collections    
import heapq
from collections import deque
import functools
# from numba import njit
import numpy as np
import bisect

def function( nums, target):
    n = len(nums)
    P = 10**9 + 7
    f = [1] + [0] * (n - 1)
    for i in range(1, n):
        f[i] = f[i - 1] * 2 % P

    nums.sort()
    ans = 0
    for i, num in enumerate(nums):
        if nums[i] * 2 > target:
            break
        maxValue = target - nums[i]
        pos = bisect.bisect_right(nums, maxValue) - 1
        contribute = f[pos - i] if pos >= i else 0
        ans += contribute
    
    return ans % P
something = function([3,3,6,8],10)
print(something)