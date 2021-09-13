'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-09-13 15:45:41
'''
import copy
import heapq
import math
from bisect import *
from collections import *
from functools import *
from itertools import *
from typing import *

import numpy as np
from scipy.special import comb, perm
# from sortedcontainers import SortedList

from utils import *

null = None
# from sortedcontainers import SortedList

class Solution:
    def __init__(self):
        pass
    def function(self, points: List[List[int]]) -> int:
        ans = 0
        for [xi, yi] in points:
            d = Counter()
            for [xj, yj] in points:
                if xi == xj and yi == yj: continue
                dist = (xi-xj)**2 + (yi-yj)**2
                d[dist] += 1
            for _, v in d.items():
                if v >= 2:
                    ans += v * (v-1)
        return ans

        
            
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])

S = Solution()
something = S.function([[0,0],[1,0],[-1,0],[0,1],[0,-1]])
print(something)
