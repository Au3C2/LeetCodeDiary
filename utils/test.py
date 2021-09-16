'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-09-14 10:35:15
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
    def function(self, s: str, dictionary: List[str]) -> str:
        # dicts = []
        m = len(s)
        for i, word in enumerate(dictionary):
            dictionary[i] = (-len(word), word)
        dictionary.sort(key=lambda d:(d[0], d[1]))
        # print(dictionary)
        for n, word in dictionary:
            i, j = 0, 0 
            n = -n
            while i < m and j < n:
                if s[i] == word[j]:
                    j += 1
                i += 1
            if j == n:
                return word
        return ''
        
            
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])

S = Solution()
something = S.function("abpcplea",["ale","apple","monkey","plea"])
print(something)
