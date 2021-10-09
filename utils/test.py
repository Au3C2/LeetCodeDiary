'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-10-08 10:53:42
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
    def function(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []
        ans, seen = set(), set()
        for i in range(n-9):
            sub = s[i:i+10]
            if sub in seen:
                ans.add(sub)
            seen.add(sub)
        return list(ans)
            
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])

S = Solution()
something = S.function("AAAAAAAAAAA")
print(something)
