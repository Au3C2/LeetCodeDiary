'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-06-25 13:13:47
'''
import collections
import heapq
from collections import deque
from functools import *
import numpy as np
import bisect
import math
from scipy.special import comb, perm
from utils import *
from typing import *
null = None
# from sortedcontainers import SortedList


class Solution:
    def __init__(self):
        pass

    def function(self, deadends: List[str], target: str) -> int:
        # deadends转化为set加速in check
        if "0000" in (deadends := set(deadends)):
            return -1
        elif target == "0000":
            return 0

        # BFS由一个 双端队列q 和 一个字典d {存遍历过的字符串: 需要旋转次数}组成，组成namedtuple
        BFS = namedtuple("BFS", "q, d")
        s, e = BFS(deque(["0000"]), {"0000": 0}), BFS(deque([target]), {target: 0})
        while s.q and e.q:
            # 选一个短的q拓展, 降低解空间复杂度
            if len(s.q) > len(e.q):
                s, e = e, s
            for _ in range(len(s.q)):
                c = s.q.popleft()
                for nxt in [
                    # 需要操作的位先转化为int, 加减1后%10，在转化为str，再和剩余位拼接
                    c[:i] + str((int(v) + x) % 10) + c[i + 1 :]
                    for x in (-1, 1)
                    for i, v in enumerate(c)
                ]:
                    # 双向BFS交集，求得解空间
                    if nxt in e.d:
                        return s.d[c] + e.d[nxt] + 1
                    elif nxt not in s.d and nxt not in deadends:
                        s.q.append(nxt)
                        s.d[nxt] = s.d[c] + 1
        return -1
        pass
        
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function( deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888")
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)
