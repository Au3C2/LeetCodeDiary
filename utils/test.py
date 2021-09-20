'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-09-17 12:03:43
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
    def function(self, board: List[List[str]]) -> bool:
        for i in range(9):
            r, c = set(), set()
            for j in range(9):
                # 检测行
                ch = board[i][j]
                if ch != '.':
                    if ch in r:
                        return False
                    else:
                        r.add(ch)
                # 检测列
                ch = board[j][i]
                if ch != '.':
                    if ch in c:
                        return False
                    else:
                        c.add(ch)
        for i in [0,3,6]: # 控制大九宫格的行
            for j in [0,3,6]: # 控制大九宫格的列
                s = set()
                for m in range(3):  # 控制小九宫格的行
                    for n in range(3): # 控制小九宫格的列
                        ch = board[i+m][j+n]
                        if ch != '.':
                            if ch in s:
                                return False
                            else:
                                s.add(ch)
        return True
        
            
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])

S = Solution()
something = S.function(
   [[".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]])
print(something)
