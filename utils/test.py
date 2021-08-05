'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-08-05 15:59:18
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
                    
    def function(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        iG = [ [] for _ in range(n) ] # 反向图
        ic = [0] * n # 图的入度图
        for s, es in enumerate(graph): # start, end
            for e in es:
                iG[e].append(s)
                # ic[e] += 1
            ic[s] = len(es)
        q = deque([i for i, n in enumerate(ic) if n == 0])
        while q:
            cur = q.popleft()
            for nei in iG[cur]:
                ic[nei] -= 1
                if ic[nei] == 0:
                    q.append(nei)
        return [i for i, n in enumerate(ic) if n == 0]

# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(graph = [[4,9],[3,5,7],[0,3,4,5,6,8],[7,8,9],[5,6,7,8],[6,7,8,9],[7,9],[8,9],[9],[]])
print(something)
