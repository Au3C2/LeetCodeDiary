'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-07-22 16:11:19
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
                    
    def function(self, head: 'Node') -> 'Node':
        h = Node(-1,head)
        p = h.next
        while p:
            node = Node(p.val, p.next)
            p.next = node
            p = node.next
        p = h.next
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        p = h.next.next
        while p:
            if p.next:
                p.next = p.next.next
            p = p.next
        return h.next.next
        
 
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function( buildList([0,9,1,2,4]),  buildList([3,2,4]))
print(something)
