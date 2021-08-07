'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-08-07 11:36:42
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
                    
    def function(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            path = [-1] * n
            path[i] = 0
            next_i = (i+nums[i])%n
            step = 0
            while nums[i] * nums[next_i] > 0 and i != next_i: # 保证下一步是同号
                if path[next_i] != -1 and step - path[next_i] > 0:
                    return True
                step += 1
                path[next_i] = step
                i, next_i = next_i, (next_i+nums[next_i])%n

        return False


# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(nums = [3,1,2])
print(something)
