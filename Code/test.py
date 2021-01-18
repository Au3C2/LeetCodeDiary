'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-01-17 19:29:26
'''
import collections    
import heapq
from collections import deque
import functools
# from numba import njit
import numpy as np
import bisect
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(tree:list):
    n = len(tree)
    level = math.ceil(math.log(n,2))
    root = TreeNode(tree[0])
    lastLevel = [root]
    m = 1
    for i in range(1,level):
        thisLevel = []
        for j in range(2**i):
            if m == n:
                return root
            if tree[m]:
                node = TreeNode(tree[m])
                thisLevel.append(node)
                if j % 2 == 0:
                    lastLevel[j//2].left = node
                else: 
                    lastLevel[j//2].right = node
            m += 1
        lastLevel = thisLevel
    return root

def function(coordinates):
    n = len(coordinates)
    c = coordinates
    for i in range(2,n):
        if (c[i][0]-c[0][0])*(c[1][1]-c[0][1]) != \
            (c[i][1]-c[0][1])*(c[1][0]-c[0][0]):
            return False
    return True

# root = buildTree([2,1,3,None,4,None,7])                          

something = function([[1,1],[2,0],[1,-1]])
print(something)