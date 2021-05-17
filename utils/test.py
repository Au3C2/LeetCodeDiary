'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-05-17 10:25:20
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
    def function(self, root: TreeNode, x: int, y: int) -> bool:
        queue = collections.deque()
        queue.append((root,None))
        while queue:
            size = len(queue)
            isCousion = None
            for _ in range(size):
                cur = queue.popleft()    
                if not cur[0]:
                    continue  
                if cur[0].val == x or cur[0].val == y:  
                    if isCousion == None:
                        isCousion = cur[1]
                    elif cur[1] != isCousion:       
                        return True
                    else:
                        return False
                if cur[0].left:
                    queue.append((cur[0].left,cur[0]))
                if cur[0].right:
                    queue.append((cur[0].right,cur[0]))
        return False

            
# root1 = buildTree([1])
# root2 = buildTree([2])      
# head = buildList([1,2,3,4,5])      
S = Solution()
something = S.function(root = buildTree([1,2,3,null,4]), x = 2, y = 3)
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# something = S.function([" /","/ "])
print(something)