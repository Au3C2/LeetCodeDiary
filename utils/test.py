'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-08-10 11:02:27
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
                    
    def function(self, nums: List[int]) -> int:
        if (n:=len(nums)) < 3:
            return 0
        diff = [nums[i]-2*nums[i-1]+nums[i-2] for i in range(2,n)]
        count, ans = 0, 0
        for d in diff:
            if d:
                count = 0
                continue
            count += 1
            ans += count            
        return ans


# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function([1,2,3,4,5,6,7,8,0,1,2,4,6,8,10])
print(something)
