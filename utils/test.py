'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-07-24 10:40:41
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
        self.MAX_SIZE = 10 ** 9 + 7
        pass
                    
    def function(self, time: str) -> str:
        if time[0] == '?':
            # time[0] = '2'
            time = '2' + time[1:]
        if time[1] == '?':
            if time[0] == '2':
                # time[1] = '3'
                time = time[0] + '3' + time[2:]
            else:
                time = time[0] + '9' + time[2:]
        if time[3] == '?':
            time = time[:3] + '5' + time[4]
        if time[4] == '?':
            time = time[:4] + '9'
        return time

 
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function( time = "2?:?0")
print(something)
