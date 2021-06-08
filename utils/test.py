'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-06-08 10:49:15
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

    def function(self, stones: List[int]) -> int:
        sumN = sum(stones)
        n = len(stones)
        neg = sumN//2
        dp = [0]*(neg+1)
        for i in range(1,n+1):
            for j in range(neg,-1,-1):
                # dp[i][j] = dp[i-1][j]
                if j >= stones[i-1]:
                    dp[j] = max(dp[j],dp[j-stones[i-1]] + stones[i-1])
        return abs(sumN - dp[neg]*2)
        
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(stones = [31,26,33,21,40])
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)
