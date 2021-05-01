'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-04-30 10:08:22
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
    def function(self, nums):
        counter = collections.Counter(nums)
        for key,value in counter.items():
            if value == 1: 
                return key

null = None
# root = buildTree([-10,9,20,null,null,15,7])
# t2 = buildTree([2,1,3,null,4,null,7])      
# head = buildList([1,2,3,4,5])      
S = Solution()
something = S.function(nums = [0,1,0,1,0,1,99])
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)