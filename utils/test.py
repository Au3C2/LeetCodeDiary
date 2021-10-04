'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-10-03 11:34:21
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
    def function(self, numerator: int, denominator: int) -> str:
        if numerator * denominator < 0:  # 判断正负
            a = '-'
            numerator = abs(numerator)
            denominator = abs(denominator)
        else:
            a = ''

        a += str(numerator // denominator)  # 将整数部分放到a中
        numerator = numerator % denominator * 10

        if numerator == 0:  # 判断是否为整数，整数就直接返回
            return a

        appeared = {numerator:0}  # 模拟小学除法，appeared为记录出现过的被除数
        resultstr = ''  # resultstr记录小数部分
        i = 0
        while numerator != 0:  # 循环除
            resultstr = resultstr + str(numerator // denominator)
            numerator = numerator % denominator * 10
            i += 1
            if numerator in appeared:  # 如果被除数出现过，证明从它上一次出现的位置产生了循环小数，跳出while循环
                break
            else:
                appeared[numerator] = i
        else:
            return a + '.' + resultstr

        place = appeared[numerator]  # index找到位置，并在两边加上括号即可
        return a + '.' + resultstr[:place] + '(' + resultstr[place:] + ')'

                
            
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])

S = Solution()
something = S.function(4, 333)
print(something)
