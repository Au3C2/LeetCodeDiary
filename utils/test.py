'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-08-16 18:15:49
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
    def function(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        ng = len(group)
        dp = [[0] * (minProfit+1) for _ in range(n+1)]
        for j in range(n+1):
            dp[j][0] = 1
        for p, g  in zip(profit, group):
            for j in range(n, g-1, -1):
                for k in range(minProfit, -1, -1):
                    dp[j][k] = (dp[j-g][max(k-p,0)] + dp[j][k]) % MOD
        return dp[n][minProfit]

# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(n = 5, minProfit = 3, group = [2,2], profit = [2,3])
print(something)
