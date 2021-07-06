'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-07-06 12:53:28
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

    def function(self, orders: List[List[str]]) -> List[List[str]]:
        orderTable = defaultdict(Counter)
        foodSet = set()
        for (_, table, food) in orders:
            orderTable[table][food] += 1
            foodSet.add(food)
        foodSet = sorted(list(foodSet))
        tableList = sorted(list(orderTable.keys()),key=lambda x:int(x))
        ans = [['Table']+foodSet]
        # ans[0].extend(foodSet)
        for table in tableList:
            tableFood = [table]
            for food in foodSet:
                tableFood.append(str(orderTable[table][food]))
            ans.append(tableFood)
        return ans
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]])
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)
