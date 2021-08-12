'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-08-12 10:41:52
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
from sortedcontainers import SortedList

from utils import *

null = None
# from sortedcontainers import SortedList

class Solution:
    def __init__(self):
        pass
                    
    def function(self, s: str) -> int:
        n = len(s)
        curRow, nxtRow = [0] * n, [0] * n
        # 从下往上遍历
        for i in range(n - 1, -1, -1):
            curRow[i] = 1
            for j in range(i + 1, n, 1):
                if s[i] == s[j]:
                    curRow[j] = nxtRow[j-1] + 2
                else:
                    curRow[j] = max(nxtRow[j],curRow[j-1])
            nxtRow, curRow = curRow, [0] * n
        return nxtRow[n - 1]


# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(s = "cbbd")
print(something)
