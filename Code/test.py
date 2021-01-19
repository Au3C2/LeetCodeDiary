'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-01-19 16:56:08
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

def function(n1,n2):
    
    if n1 and n2:
        n1.val += n2.val
        n1.left = function(n1.left,n2.left)
        n1.right = function(n1.right,n2.right)
    elif n1:
        pass
    elif n2:
        return n2
    else:
        return None
    
    return n1
    
null = None
t1 = buildTree([1,3,2,5])  
t2 = buildTree([2,1,3,null,4,null,7])                   
something = function(t1,t2)
print(something)