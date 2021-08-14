'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-08-14 11:34:14
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
    def function(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        n = len(preferences)
        prefer_index = [[-1] * n for _ in range(n)]
        for i in range(n):
            for j in range(n-1):
                prefer_index[i][preferences[i][j]] = j # 快速索引朋友的排序
        pairs_d = [0] * n
        for x, y in pairs:
            pairs_d[x] = y
            pairs_d[y] = x
        unhappy = set()
        
        # 挨个检查每个人
        for x in range(n):
            if x in unhappy:
                continue
            y = pairs_d[x] # x 的对象
            idx_y = prefer_index[x][y] # y在x的排序
            # 搜索 x 中排在 y 前面的朋友，并且挨个检查
            for u in preferences[x][:idx_y]:
                # 检查u的配对
                v = pairs_d[u]
                if prefer_index[u][x] < prefer_index[u][v]:
                    unhappy.add(x)
                    unhappy.add(u)
        return len(unhappy)


# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(4,
[[1,3,2],[0,2,3],[3,1,0],[2,0,1]],
[[2,1],[3,0]])
print(something)
