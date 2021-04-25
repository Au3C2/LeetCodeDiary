'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-04-22 14:16:25
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
from sortedcontainers import SortedList
class Solution:
    def __init__(self):
        pass
    def function(self,matrix,k):
        m, n = len(matrix), len(matrix[0])
        cum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                cum[i][j] = cum[i-1][j] + cum[i][j-1] - cum[i-1][j-1] + matrix[i-1][j-1]
        ans = -float('inf')
        for x1 in range(1,m+1):
            for y1 in range(1,n+1):
                for x2 in range(x1,m+1):
                    for y2 in range(y1,n+1):
                        cur = cum[x2][y2] - cum[x1-1][y2] - cum[x2][y1-1] + cum[x1-1][y1-1]
                        if cur <= k:
                            ans = max(cur,ans)
        return ans
null = None
# root = buildTree([-10,9,20,null,null,15,7])
# t2 = buildTree([2,1,3,null,4,null,7])      
# head = buildList([1,2,3,4,5])      
S = Solution()
something = S.function(matrix = 
[[5,-4,-3,4],
[-3,-4,4,5],
[5,1,5,-4]], k = 3)
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)