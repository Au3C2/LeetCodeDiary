'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-09-22 12:14:52
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
    def function(self, head: ListNode, k: int) -> List[ListNode]:
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        ans, cur = [], head
        if n <= k:
            while cur:
                ans.append(cur)
                cur.next, cur = None, cur.next
            while k - n > 0:
                ans.append(None)
                n += 1
        else:
            i, m, pre, j = 0, n//k, None, n%k
            while i<(m+1)*j:
                if i%(m+1) == 0:
                    ans.append(cur)
                    if pre: 
                        pre.next = None
                pre, cur = cur, cur.next
                i += 1
            while i < n:
                if (i-(m+1)*j)%m == 0:
                    ans.append(cur)
                    if pre: 
                        pre.next = None
                pre, cur = cur, cur.next
                i += 1
        return ans
        
            
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])

S = Solution()
something = S.function(buildList([1,2,3,4,5,6,7,8,9,10]), 4)
print(something)
