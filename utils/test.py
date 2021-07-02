'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-07-02 09:49:51
'''
import collections
import heapq
from collections import defaultdict, deque
from functools import *
import numpy as np
import bisect
import math
from scipy.special import comb, perm
from utils import *
from typing import *
import copy
null = None
# from sortedcontainers import SortedList


class Solution:
    def __init__(self):
        pass

    def function(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i = 0
        while coins >= 0 and i <len(costs):
            coins -= costs[i]
            i += 1
        return i if coins >=0 else i - 1
        pass
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(costs = [1,6,3,1,2,5], coins = 20)
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)
