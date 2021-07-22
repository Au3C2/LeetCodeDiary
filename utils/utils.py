'''
Description: 
Autor: Au3C2
Date: 2021-03-25 20:31:55
LastEditors: Au3C2
LastEditTime: 2021-07-22 13:34:36
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
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
def buildTree(data:list):
    if not data: return
    n = len(data)
    queue = list()
    queue.append(TreeNode(data[0]))
    res = queue[0]
    if n == 1: return res
    i = 1
    while queue:
        size = len(queue)
        level = list()
        for _ in range(size):
            cur = queue.pop(0)
            if data[i] != None:
                t = TreeNode(data[i])
                cur.left = t
                level.append(t)
            i += 1
            if i == n:
                return res
            if data[i] != None:
                t = TreeNode(data[i])
                cur.right = t
                level.append(t)
            i += 1
            if i == n:
                return res
        queue = level
    return res

''' 被废弃的写法
def buildTree_old(tree:list):
    if not tree: return
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
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def buildList(l: list) -> ListNode:
    head = None
    last_node = None
    for n in l:
        if not head:
            head = ListNode(n)
            last_node = head
        else:
            node = ListNode(n)
            last_node.next = node
            last_node = node
    return head       