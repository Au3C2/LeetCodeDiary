'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-04-28 12:19:07
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
    def function(self, c):
        b = 0
        t = c - b**2
        while t >= 0 :
            a = math.sqrt(t)
            if a % 1 == 0:
                return True
            else:
                b += 1
                t = c - b**2
        return False
null = None
# root = buildTree([-10,9,20,null,null,15,7])
# t2 = buildTree([2,1,3,null,4,null,7])      
# head = buildList([1,2,3,4,5])      
S = Solution()
something = S.function(c = 0)
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)