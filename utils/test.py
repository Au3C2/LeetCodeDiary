'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-06-24 12:10:37
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

    def function(self, points: List[List[int]]) -> int:
        ans = 1
        n = len(points)
        for i in range(n-1):
            counter = Counter()
            for j in range(i+1,n):
                dx, dy = points[i][0] - points[j][0], points[i][1] - points[j][1]
                counter[dy/dx if dx else 'inf'] += 1
            ans = max(ans,max(counter.values())+1)
        return ans
        pass
        
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(points = [[1,1],[2,2],[3,3]])
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)
