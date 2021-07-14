'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-07-14 12:59:00
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

    def function(self, nums1: List[int], nums2: List[int]) -> int: 
        nums1Sorted = sorted(nums1)
        ans, nd = 0, 0
        for i in range(n:=len(nums1)):
            diff = abs(nums1[i] - nums2[i])
            if diff == 0: continue
            idx = bisect.bisect(nums1Sorted,nums2[i])
            if idx < n:
                nd = max([diff-abs(nums1Sorted[idx]-nums2[i]), nd])
            if idx > 1:
                nd = max([diff-abs(nums1Sorted[idx-1]-nums2[i]), nd])
            if idx < n-1:
                nd = max([diff-abs(nums1Sorted[idx+1]-nums2[i]), nd])
            if idx >= n-1:
                nd = max([diff-abs(nums1Sorted[-1]-nums2[i]), nd])
            ans += diff
        return (ans - nd) % self.MAX_SIZE
        pass
        
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(nums1 = [1,7,5], nums2 = [2,3,5])
print(something)
