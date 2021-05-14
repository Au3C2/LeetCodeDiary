'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-05-14 10:19:09
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
# from sortedcontainers import SortedList
class Solution:
    def __init__(self):
        pass
    def function(self, num: int) -> str:
        res = ''
        i = 0
        ROMES = [['I','V'],['X','L'],['C','D'],['M']]
        while num > 0:
            figure = num % 10
            if 0 <= figure and figure <= 3:
                rome = ROMES[i][0]*figure
            elif figure == 4:
                rome = ROMES[i][0]+ROMES[i][1]
            elif 5 <= figure and figure < 9:
                rome = ROMES[i][1]+ROMES[i][0]*(figure-5)
            elif figure == 9:
                rome = ROMES[i][0] + ROMES[i+1][0]
            res = rome + res
            i += 1
            num = num // 10
        return res

# null = None
# root1 = buildTree([1])
# root2 = buildTree([2])      
# head = buildList([1,2,3,4,5])      
S = Solution()
something = S.function(num = 58)
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)