'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-01-28 10:23:41
'''
import collections    
import heapq
from collections import deque
import functools
# from numba import njit
import numpy as np
import bisect
import math
from scipy.special import comb, perm
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
    lastLevel = list([root])
    m = 1
    for i in range(1,level):
        thisLevel = list()
        for j in range(2**i):
            if m == n:
                return root
            if tree[m] != None:
                node = TreeNode(tree[m])
                thisLevel.append(node)
                if j % 2 == 0:
                    lastLevel[j//2].left = node
                else: 
                    lastLevel[j//2].right = node
            m += 1
        lastLevel = thisLevel
    return root


def function(nums):
    n = len(nums)
    if not nums:
        return -1
    leftSum = 0
    rightSum = sum(nums)-nums[0]
    for i in range(n-1):
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
        rightSum -= nums[i+1]
    if leftSum == rightSum:
        return i + 1
    return -1

        
# null = None
# root = buildTree([4,2,5,1,3,null,6,0])  
# t2 = buildTree([2,1,3,null,4,null,7])            
something = function([-1,-1,0,1,1,0])
print(something)