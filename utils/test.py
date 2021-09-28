'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-09-28 10:59:24
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
    def function(self, root: TreeNode, targetSum: int) -> int:
        #对树做前序遍历同时做前缀和，同时记录祖先中的前缀和，在回溯时删除
        prefix_sum = defaultdict(int) #记录路径中不同前缀和的数量
        prefix_sum[0] = 1 #哨兵，没有节点时和为0
        pre = 0 #从根节点到当前节点位置该路径的前缀和
        ans = 0
        def preOrder(root):
            nonlocal pre,prefix_sum,targetSum,ans
            if not root:
                return
            pre += root.val
            ans += prefix_sum[pre-targetSum]
            prefix_sum[pre] += 1

            preOrder(root.left)
            preOrder(root.right)

            prefix_sum[pre] -= 1
            pre -= root.val
        
        preOrder(root)
        return ans
       
            
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])

S = Solution()
something = S.function(root = buildTree([10,5,-3,3,2,null,11,3,-2,null,1]), targetSum = 8)
print(something)
