'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-03-26 10:10:13
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
from utils import *
class Solution:
    def __init__(self):
        print('init...')
        
    def function(self,head):
        if not head: return
        t = ListNode(None)
        t.next = head
        head = t
        preNode = head
        thisNode = preNode.next
        postNode = thisNode.next
        while postNode:
            while postNode and thisNode.val == postNode.val:
                postNode = postNode.next
                # preNode.next = postNode
                # flag = True
            thisNode.next = postNode
            if not postNode:break
            # if not flag:
            #     preNode = thisNode
            thisNode = postNode
            postNode = postNode.next
            # flag = False
        return head.next

                                        
null = None
# root = buildTree([-10,9,20,null,null,15,7])
# t2 = buildTree([2,1,3,null,4,null,7])      
# head = buildList([1,2,3,4,5])      
S = Solution()
# something = S.function(2)
something = S.function(buildList([1,1,2]))
print(something)