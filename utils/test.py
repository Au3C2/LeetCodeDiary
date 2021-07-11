'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-07-11 13:30:30
'''
import collections
import heapq
from collections import defaultdict, deque
from functools import *
import numpy as np
from bisect import *
import math
from scipy.special import comb, perm
from utils import *
from typing import *
import copy
from itertools import *
null = None
# from sortedcontainers import SortedList


class Solution:
    def __init__(self):
        pass

    def function(self,  citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i,c in enumerate(citations):
            h = n - i
            if h <= c:
                return h
        return 0
        
        pass
        
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(citations = [3,0,6,1,5])
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)
