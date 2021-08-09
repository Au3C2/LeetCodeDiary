'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-08-09 10:58:02
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
                    
    def function(self, n: int, primes: List[int]) -> int:
        if n < 0:
            return 0
        dp = [float('inf')] * n
        dp[0] = 1
        np = len(primes)
        index = [0] * np
        for i in range(1, n):
            for j in range(np):
                if primes[j] * dp[index[j]] <= dp[i]:
                    dp[i] = primes[j] * dp[index[j]]
            for j in range(np):
                if dp[i] == primes[j] * dp[index[j]]:
                    index[j] += 1
        return dp[n-1]


# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(n = 12, primes = [2,7,13,19])
print(something)
