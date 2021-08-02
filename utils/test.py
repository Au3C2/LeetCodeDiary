'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-08-02 13:08:18
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
                    
    def function(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for t in times:
            g[t[0]].append((t[1],t[2]))
        q = deque([(k, 0)])
        visited = {k:0}
        while q:
            q_len = len(q)
            for _ in range(q_len):
                cur, t = q.popleft()
                for nei, w in g[cur]:
                    if (nei in visited and w+t < visited[nei]) or nei not in visited:
                        q.append((nei, w+t))
                        visited[nei] = w+t
        if len(visited) != n:
            return -1
        time = -1
        for k, v in visited.items():
            time = max(time,v)
        return time
 
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)
print(something)
