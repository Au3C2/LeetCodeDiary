'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-07-29 10:35:23
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
        self.POWER2 = [1]
        for i in range(20):
            self.POWER2.append(self.POWER2[-1]*2)
        pass
                    
    def function(self, label: int) -> List[int]:
        for n in range(20):
            if label < self.POWER2[n]:
                break
        # print(n)
        n -= 1
        ans = [label]
        for i in range(n,0,-1):
            ans.append(self.POWER2[i]-1-ans[-1]//2+self.POWER2[i-1])
        
        return ans[::-1]
 
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(label = 656356)
print(something)
