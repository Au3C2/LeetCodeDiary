'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-08-20 14:23:38
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
    def function(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        i = -1
        for i in range(n//(2*k)):
            t = s[i*2*k:i*2*k+k]
            s[i*2*k:i*2*k+k] = t[::-1]
        i += 1
        if n % (2*k) >= k:
            t = s[i*2*k:i*2*k+k]
            s[i*2*k:i*2*k+k] = t[::-1]
        else:
            t = s[i*2*k:]
            s[i*2*k:] = t[::-1]
        return ''.join(s)

# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function("abcd",3)
print(something)
