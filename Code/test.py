'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-03-11 12:20:46
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
    stack = []
    lastFlag = False
    n = len(s)
    i = 0    
    while i < n :

        if s[i].isdigit():
            t = list(s[i])
            while i<n-1 and s[i+1].isdigit():
                t.append(s[i+1])
                i += 1
            i += 1
            stack.append(''.join(t))
            
            if lastFlag:
                num2, operator, num1 = int(stack.pop()), stack.pop(), int(stack.pop())
                t = num1 * num2 if operator == '*' else math.floor(num1 / num2)
                stack.append(str(t))
                lastFlag = False

        else:
            stack.append(s[i])
            if s[i]=='*' or s[i] == '/':
                lastFlag = s[i]
            i += 1
        
        # if s[i]=='*' or s[i] == '/':
        #     lastFlag = s[i]
            
    return eval(''.join(stack))
           
# null = None
# root = buildTree([4,2,5,1,3,null,6,0])  
# t2 = buildTree([2,1,3,null,4,null,7])            
something = function("3+2*2")
print(something)