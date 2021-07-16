'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-07-16 10:21:43
'''
import collections
import copy
import heapq
import math
from bisect import *
from collections import defaultdict, deque
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
        self.MAX_SIZE = 10 ** 9 + 7
        pass
                    
    def function(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        lp, rp = idx-1, idx
        ans = 0
        while lp >= 0:
            if nums[lp] == target:
                ans += 1
            else:
                break
            lp -= 1
        lp += 1
        while rp < len(nums):
            if nums[rp] == target:
                ans += 1
            else:
                break
            rp += 1
        rp -= 1
        return [lp, rp] if ans else [-1,-1]
        
        
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(nums = [1], target = 1)
print(something)
