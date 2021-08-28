'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-08-28 22:06:50
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
    def function(self, dicts, s):
        n = len(s)
        @lru_cache()
        def recursion(s):
            if not s:
                return True
            res = False
            for i in range(1, len(s)+1):
                if s[:i] in dicts:
                    res = recursion(s[i:]) or res
            return res
        return recursion(s)
        
            
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(["cat", "dog", "cats", "and", "sand"]
, "catsanddog")
print(something)
