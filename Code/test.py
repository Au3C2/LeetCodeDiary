'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-01-20 10:57:00
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
    level = math.ceil(math.log(n+1,2))
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

def function(root,low,high):
    if not root:
        return 0
    if low < root.val < high:
        leftSum = function(root.left,low,high)
        rightSum = function(root.right,low,high)
        return root.val + leftSum + rightSum
    elif root.val <= low:
        rightSum = function(root.right,low,high)
        if root.val == low:
            return rightSum + root.val  
        else:
            return rightSum
    elif root.val >= high:
        leftSum = function(root.left,low,high)
        if root.val == high:
            return leftSum + root.val  
        else:
            return leftSum   
    
null = None
root = buildTree([10,5,15,3,7,13,18,1,null,6])  
# t2 = buildTree([2,1,3,null,4,null,7])                   
something = function(root,low = 6, high = 10)
print(something)