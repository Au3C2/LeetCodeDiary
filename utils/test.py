'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-07-26 14:59:02
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
                    
    def function(self, target: List[int], arr: List[int]) -> int:
        q, d = [], {x: i for i, x in enumerate(target)}
        for x in arr:
            if x in d:
                i = bisect_left(q, d[x])
                q[i:i+1] = d[x],
        return len(target) - len(q)

 
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1,4])
print(something)

# 新增的数只要比前一位大（也就是d的最后一位）,那就说明这个数字可以起到延长序列的作用，所以append上；否则， 
# 如果新增的数比前一位小（严格增的话，这里包含等于），那就说明这个数字直接拼上前一位元素，不能起到延长序列的作用（构不成严格增序列）， 
# 又因为d中存的是每一个长度末尾最小的元素，且d中现存的元素都是在nums[i]之前出现过的，因此找到nums[i]在d上的位置，并不会影响子序列的顺序。 
# nums[i]要是比d中所有值都小，那说明这个数只能打头，所以就放到第一位； 
# 如果nums[i]在d中的位置在第2位，那说明第一位曾经出现过的数字可以和该数字构成一个长度为2的子序列 
# 只不过由于贪心的思想，不得不找更小的末尾元素在适合的长度上。 
# 如果还理解不了，需要记住，无论是d中现有的数字还是被替换掉的数字，在nums中的顺序都在nums[i]之前，因此只需要判断大小即可，位置是没有变的 
# 或者可以这样理解：d的长度就是最长序列的长度