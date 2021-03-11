'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-03-11 15:01:18
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


def function(s):
    s = s.replace(' ','')
    stack = list()
    lastOpra = False
    n = len(s)
    i = 0    
    while i < n :

        if s[i].isdigit():
            num2 = int(s[i])
            while i<n-1 and s[i+1].isdigit():
                num2 = num2*10 + int(s[i+1])
                i += 1
            i += 1
            if lastOpra =='*' or lastOpra == '/':
                num1 = stack.pop()
                t = num1 * num2 if lastOpra == '*' else int(num1 / num2)
                stack.append(t)
                lastOpra = False
            elif lastOpra=='-':
                stack.append(-1*num2)
            else:
                stack.append(num2)
        else:
            lastOpra = s[i]
            i += 1           
    return sum(stack)
           
# null = None
# root = buildTree([4,2,5,1,3,null,6,0])  
# t2 = buildTree([2,1,3,null,4,null,7])            
something = function("14-3/2")
print(something)