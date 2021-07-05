'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-07-05 12:41:46
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

    def function(self, formula: str) -> str:
        # 倒着的时候， 记录map，乘的基数，迭代中的乘数，个数，个数的10进制位数，元素
        cnts, multiply, muls, num, num_count, atom = defaultdict(int), 1, [], 0, 0, ""
        for c in formula[::-1]:
            if c == ')':
                # 如果当前有统计的数字，乘的基数要叠加
                if num:
                    multiply *= num
                    muls.append(num)
                    num = num_count = 0
                else:
                    muls.append(multiply)
            elif c == '(':
                # 去除掉上一个乘数
                multiply //= muls.pop()
            elif str.isdigit(c):
                num += int(c) * (10 ** num_count)
                num_count += 1
            elif str.islower(c):
                atom += c
            else: # c是大写字母
                atom += c
                # 注意我们在更新元素个数时，始终要考虑乘的基数
                if num:
                    cnts[atom[::-1]] += num * multiply
                else:
                    cnts[atom[::-1]] += multiply
                atom = ""
                num = num_count = 0
        return "".join(key if cnts[key] == 1 else key + str(cnts[key]) for key in sorted(cnts.keys()))
            
        pass
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(formula = "(B2O39He17BeBe49)39")
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)
