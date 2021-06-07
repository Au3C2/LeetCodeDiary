'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-06-07 10:58:08
'''
import collections
import heapq
from collections import deque
from functools import *
import numpy as np
import bisect
import math
from scipy.special import comb, perm
from utils import *
from typing import *
null = None
# from sortedcontainers import SortedList


class Solution:
    def __init__(self):
        pass

    def function(self, nums: List[int], target: int) -> int:
        sumN = sum(nums)
        diff = sumN-target
        if diff<0 or diff%2 != 0:
            return 0
        n = len(nums)
        neg = diff//2
        row = [0]*(neg+1)
        row[0] = 1
        for i in range(1,n+1):
            for j in range(neg,-1,-1):
                if j >= nums[i-1]:
                    row[j] += row[j-nums[i-1]]
        return row[neg]      
        
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(nums = [1,0], target = 1)
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)
