'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-06-22 11:06:36
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

    def function(self, s: str) -> List[str]:
        def recursion(s:str):
            if not s: 
                return ''
            else:
                ans = []
                for i,c in enumerate(s):
                    res = recursion(s[:i]+s[i+1:])
                    if res == '':
                        ans.append(c)
                    for r in res:
                        ans.append(c+r)
            return ans
        ans = recursion(s)
        return ans
        pass
        
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(s = "abc")
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)
