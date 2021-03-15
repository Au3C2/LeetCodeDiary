'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-03-15 12:42:56
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


def function(matrix):
    m, n = len(matrix), len(matrix[0])
    direc = [[0,1],[1,0],[0,-1],[-1,0]]
    bound = [1,0,m-1,n-1] # 上左下右边界
    res = list()
    d = 0
    x = 0
    y = 0
    i = 0
    while 1:
        res.append(matrix[x][y])
        i += 1
        if i == m*n:
            break

        if direc[d][0] == 1 and x == bound[2]: #向下移动碰到边界
            d = (d+1)%4
            bound[2] -= 1
        if direc[d][0] == -1 and x == bound[0]:#向上移动碰到边界
            d = (d+1)%4
            bound[0] += 1

        if direc[d][1] == 1 and y == bound[3]:#向右移动碰到边界
            d = (d+1)%4
            bound[3] -= 1    
        if direc[d][1] == -1 and y == bound[1]:#向左移动碰到边界
            d = (d+1)%4
            bound[1] += 1

        x += direc[d][0]
        y += direc[d][1]
        
    return res
# null = None
# root = buildTree([4,2,5,1,3,null,6,0])  
# t2 = buildTree([2,1,3,null,4,null,7])            
something = function([[1,2,3],[4,5,6],[7,8,9]])
print(something)