'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-02-21 11:21:56
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


def function(nums,limit):
    
           
# null = None
# root = buildTree([4,2,5,1,3,null,6,0])  
# t2 = buildTree([2,1,3,null,4,null,7])            
something = function(nums = [10,1,2,4,7,2], limit = 5)
print(something)