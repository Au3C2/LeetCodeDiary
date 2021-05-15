'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-05-15 18:18:29
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
# from sortedcontainers import SortedList
class Solution:
    def __init__(self):
        pass
    def function(self, s) -> int:
        ROMES = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        # ROMES2 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        n = len(s)
        ans = 0
        for i in range(n-1):
            if ROMES[s[i]] < ROMES[s[i+1]]:
                ans -= ROMES[s[i]]
            else:
                ans += ROMES[s[i]]
        ans += ROMES[s[-1]]
        return ans
            
# null = None
# root1 = buildTree([1])
# root2 = buildTree([2])      
# head = buildList([1,2,3,4,5])      
S = Solution()
something = S.function("LVIII")
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)