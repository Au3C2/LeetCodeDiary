'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-08-26 11:17:11
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
    def function(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        n = len(people)
        ans, lp, rp = 0, 0, n-1
        while lp <= rp:
            if lp == rp:
                rp -= 1
            if people[rp] + people[lp] <= limit:
                rp -= 1
            ans += 1
            lp += 1
        return ans         
            
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(people = [3,5,3,4], limit = 5)
print(something)
