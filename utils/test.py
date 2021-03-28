'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-03-27 09:39:11
'''
import collections    
import heapq
from collections import deque
import functools
import numpy as np
import bisect
import math
from scipy.special import comb, perm
from utils import *
class Solution:
    def __init__(self):
        print('init...')
        
    def function(self,head,k):
        thisNode = head
        n = 1
        while thisNode.next:
            n += 1
            thisNode = thisNode.next
        k = n - k % n
        thisNode.next = head
        n = 0
        while n < k:
            preNode = head
            head = head.next
            n += 1
        preNode.next = None
        return head
                                        
null = None
# root = buildTree([-10,9,20,null,null,15,7])
# t2 = buildTree([2,1,3,null,4,null,7])      
# head = buildList([1,2,3,4,5])      
S = Solution()
# something = S.function(2)
something = S.function(buildList([0,1,2]),4)
print(something)