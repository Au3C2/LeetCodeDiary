'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-06-21 10:50:10
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

    def function(self, turnedOn: int) -> List[str]:
        if turnedOn>8:
            return []
        mCount = {}
        for m in range(60):            
            bits = bin(m).count('1')
            s = '{:0>2d}'.format(m)
            if bits in mCount:
                mCount[bits].append(s)
            else:
                mCount[bits] = [s]
        hCount = {}
        for h in range(12):            
            bits = bin(h).count('1')
            s = '{:d}'.format(h)
            if bits in hCount:
                hCount[bits].append(s)
            else:
                hCount[bits] = [s]
        ans = []
        for i in range(turnedOn+1): # 遍历小时
            if i > 3:
                break
            if turnedOn-i>5:
                continue
            for h in hCount[i]:
                for m in mCount[turnedOn-i]:
                    ans.append(h+':'+m)
        return ans
        pass
        
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(turnedOn = 0)
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)
