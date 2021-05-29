'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-05-29 12:01:55
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
    def function(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for i in range(1, n + 1):
            presum = [0] * (m + 1)
            for j in range(i, n + 1):
                a = 0
                d = Counter([0])
                for fixed in range(1, m + 1):
                    presum[fixed] += matrix[fixed-1][j-1]
                    a += presum[fixed]
                    if a - target in d:
                        ans += d[a - target]
                    d[a] += 1
        return ans

# root1 = buildTree([1])
# root2 = buildTree([2])      
# head = buildList([1,2,3,4,5])      
S = Solution()
something = S.function(matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0)
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)