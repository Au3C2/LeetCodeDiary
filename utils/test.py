'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-06-19 12:44:40
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

    def function(self, arr: List[str]) -> int:
        n = len(arr)
        if n == 1: return len(set(arr[0]))
        binary = []
        for s in arr:
            b = 0
            for c in s:
                b |= 1 << (ord(c)-ord('a'))
            binary.append(b)
        # preXOR = []
        # for b in binary:
            
        pass
        
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(arr = ["cha","r","act","ers"])
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)
