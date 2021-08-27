'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-08-26 15:32:31
'''
import copy
import heapq
import math
from bisect import *
from collections import *
from functools import *
from itertools import *
from typing import *

import numpy as np
from scipy.special import comb, perm
# from sortedcontainers import SortedList

from utils import *

null = None
# from sortedcontainers import SortedList

class Solution:
    def __init__(self):
        pass
    def function(self, n:int, m:int, nums):
        ans = [float('inf')] * (n*m) # 返回的答案
        t = [(nums[j][0],j,0) for j in range(n)]  # 多指针
        heapq.heapify(t)
        for i in range(n * m):
            ans[i], j, idx = heapq.heappop(t)
            if idx < m - 1:
                idx += 1
                heapq.heappush(t,(nums[j][idx], j, idx))
            # idx = 0
            # for j in range(n): # 遍历查找 nums 每行
            #     if t[j] < m and nums[j][t[j]] <= ans[i]:
            #         idx = j
            #         ans[i] = nums[j][t[j]]
            # t[idx] += 1 # 当前指针向后移

        return ans
            
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(3,3,[[1,3,5],[2,4,6],[1,3,6]])
print(something)
