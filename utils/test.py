'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-07-01 10:50:57
'''
import collections
import heapq
from collections import defaultdict, deque
from functools import *
import numpy as np
import bisect
import math
from scipy.special import comb, perm
from utils import *
from typing import *
import copy
null = None
# from sortedcontainers import SortedList


class Solution:
    def __init__(self):
        pass

    def function(self, n: int, relation: List[List[int]], k: int) -> int:
        g = defaultdict(set)
        for r in relation:
            g[r[0]].add(r[1])
        if not g[0]:
            return 0
        queue = deque([0]) # 编号，第几轮
        ans = 0
        for e in range(k):
            length = len(queue)
            for _ in range(length):
                cur = queue.popleft()
                for neighbor in g[cur]:
                    if e + 1 == k and neighbor == n-1:
                        ans += 1
                    queue.append(neighbor)
        return ans           
        pass
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(n = 3, relation = [[0,2],[2,1]], k = 2)
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)
