'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-08-06 11:14:25
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
                    
    def function(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque([ (i, 1 << i) for i in range(n)])
        visited = set(q)
        step = 0
        while q:
            nq = len(q)
            for _ in range(nq):
                cur, status = q.popleft()
                for nei in graph[cur]:
                    new_status = status | (1 << nei)
                    if new_status == ((1 << n)-1):
                        return step + 1
                    if (nei,new_status) not in visited:
                        visited.add((nei, new_status))
                        q.append((nei, new_status))
            step += 1
        return 0

# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(graph = [[1,2,3,4,5,6,7,8,9,10,11],[0,2,5,6,8],[0,1,4,5,6,9,10,11],[0,4,5,6,8,9,10,11],[0,2,3,5,6,8,10],[0,1,2,3,4,6,8,9,10,11],[0,1,2,3,4,5,8,10,11],[0,8],[0,1,3,4,5,6,7,9,10,11],[0,2,3,5,8,10],[0,2,3,4,5,6,8,9],[0,2,3,5,6,8]])
print(something)
