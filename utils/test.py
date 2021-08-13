'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-08-13 13:18:47
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
    def function(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0: # 当 high 和 cur 同时为 0 时，说明已经越过最高位，因此跳出
            if cur == 0: res += high * digit
            elif cur == 1: res += high * digit + low + 1
            else: res += (high + 1) * digit
            low += cur * digit # 将 cur 加入 low ，组成下轮 low
            cur = high % 10  # 下轮 cur 是本轮 high 的最低位
            high //= 10  # 将本轮 high 最低位删除，得到下轮 high
            digit *= 10 # 位因子每轮 × 10
        return res


# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(824883294)
print(something)
