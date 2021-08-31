'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-08-29 23:43:41
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
    def function(self, arr: List[int]) -> int:
        n = len(arr)
        preSum = [0] * (n+1)
        for i in range(n):
            preSum[i+1] = preSum[i] + arr[i]
        ans = 0
        for w in range(1,n+1,2):
            for i in range(n-w+1):
                ans += (preSum[i+w] - preSum[i])
        return ans

        
            
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function([1,4,2,5,3])
print(something)
