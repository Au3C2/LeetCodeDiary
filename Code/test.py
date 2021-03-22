'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-03-22 15:59:40
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

class Solution:
    def __init__(self):
        print('init...')
    def function(self, n):
        # res = 0
        n = str(bin(n))
        counter = collections.Counter(n)
        return counter['1']
        # for c in str(bin(n)):
            
        #     res += 1

    def levelOrder(self, root):
        self.output = list()
        self.recursion(root)
        n = len(self.output)
        if n % 2 == 0:
            return False
        for i in range(n//2):
            if self.output[i] != self.output[-i-1]:
                return False

        lastLevel = collections.deque()
        lastLevel.append(root)
        while lastLevel:
            size = len(lastLevel)
            thisLevel = collections.deque()
            for _ in range(size):
                cur = lastLevel.popleft()
                if not cur:
                    continue
                # thisLevel.append(cur.val)
                if cur.left:
                    thisLevel.append(cur.left)
                if cur.right:
                    thisLevel.append(cur.right)
            n = len(thisLevel)
            for i in range(n//2):
                if thisLevel[i].val != thisLevel[-i-1].val:
                    return False
            lastLevel = thisLevel
               
        return True

    def recursion(self,root):
        
        if not root:
            return None

        if not root.left and root.right:
            root.left = TreeNode('N')
        if not root.right and root.left:
            root.right = TreeNode('N')
            
        self.recursion(root.left)         
        self.output.append(root.val) 
        self.recursion(root.right)

        # if left == None and right:
        #     t = self.output.pop()
        #     self.output.append(None)
        #     self.output.append(t)
            
        # if right == None and left:
        #     self.output.append(None)
                              
null = None
# root = buildTree([-10,9,20,null,null,15,7])
# t2 = buildTree([2,1,3,null,4,null,7])      
# head = buildList([1,2,3,4,5])      
S = Solution()
# something = S.function(0b00000000000000000000000000001011)
something = S.levelOrder(buildTree([1,2,2,3,4,4,3]))
print(something)