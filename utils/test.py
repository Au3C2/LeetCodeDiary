'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-09-26 11:27:52
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
    def function(self, a: int, b: int) -> int:
        MASK1 = 4294967296  # 2^32，1后面32个0
        MASK2 = 2147483648  # 2^31，1后面31个0
        MASK3 = 2147483647  # 2^31-1，31个1
        while b != 0:
            carry = ((a & b) << 1) % MASK1
            a = (a ^ b) % MASK1
            b = carry
        if a & MASK2:  # 负数，这里算出来是a的补码，要取反再+1成原码 
            return ~((a ^ MASK2) ^ MASK3)
        else:  # 正数
            return a
       
            
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])

S = Solution()
something = S.function(a = -2, b = 1)
print(something)
