'''
Description: 
Autor: Au3C2
Date: 2021-06-15 10:05:35
LastEditors: Au3C2
LastEditTime: 2021-07-28 10:24:51
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
                    
    def function(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g = defaultdict(list)
        def dfs(root):
            if not root: return
            if root.left:
                g[root.val].append(root.left.val)
                g[root.left.val].append(root.val)
            if root.right:
                g[root.val].append(root.right.val)
                g[root.right.val].append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        visited = [False] * 501
        queue = deque([target.val])
        for i in range(k):
            n = len(queue)
            for _ in range(n):
                cur = queue.popleft()
                visited[cur] = True
                for val in g[cur]:
                    if not visited[val]:
                        queue.append(val)
        return list(queue)
 
# root1 = buildTree([1])
# root2 = buildTree([2])
# head = buildList([1,2,3,4,5])
S = Solution()
something = S.function(buildTree([3,5,1,6,2,0,8,null,null,7,4]), TreeNode(5),2)
print(something)
