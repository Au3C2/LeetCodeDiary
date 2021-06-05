'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-06-05 11:18:47
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
null = None
# from sortedcontainers import SortedList


class Solution:
    def __init__(self):
        pass

    def function(self, head: ListNode, val: int) -> ListNode:
        if not head: return
        head0 = ListNode(0,None)
        pre = head0
        node = head
        while node:
            if node.val != val:
                pre.next = node
                pre = node
            node = node.next 
            pre.next = None           
        return head0.next

# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(head = buildList([7,7,7,7]), val = 7)
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)
