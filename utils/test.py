'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-03-31 14:30:11
'''
import collections    
import heapq
from collections import deque
import functools
import numpy as np
import bisect
import math
from scipy.special import comb, perm
from utils import *
class Solution:
    def __init__(self):
        # print('init...')
        pass
        
    def function(self,nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, res, [])
        return res
        
    def dfs(self, nums, index, res, path):
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, res, path + [nums[i]])

null = None
# root = buildTree([-10,9,20,null,null,15,7])
# t2 = buildTree([2,1,3,null,4,null,7])      
# head = buildList([1,2,3,4,5])      
S = Solution()
# something = S.function(2)
something = S.function([1,2,2])
print(something)