'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-05-22 15:07:24
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
    def function(self, nums1: List[int]):
        xor = lambda x,y:x^y
        res = reduce(xor,nums1)
        
        return res
# root1 = buildTree([1])
# root2 = buildTree([2])      
# head = buildList([1,2,3,4,5])      
S = Solution()
something = S.function(nums1 = [1,3,7,1,7,5])
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)