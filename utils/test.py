'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-07-14 17:01:34
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
                    
    def function(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        self.graph = collections.defaultdict(list)
        for pre in prerequisites:
            self.graph[pre[0]].append(pre[1])
        return [self.dfs(query[0], query[1]) for query in queries]
    
    # start -> end ?
    @lru_cache
    def dfs(self, start, end):
        if start == end:
            return True
        return any(self.dfs(nxt, end) for nxt in self.graph[start])
        pass
        
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function()
print(something)
