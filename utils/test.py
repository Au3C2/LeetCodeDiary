'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-03-29 10:46:10
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
        
    def function(self,n):
        n = list('{:032b}'.format(n))
        n.reverse()
        # n = int(n)
        return int(''.join(['0','b']+n),2)
                                        
null = None
# root = buildTree([-10,9,20,null,null,15,7])
# t2 = buildTree([2,1,3,null,4,null,7])      
# head = buildList([1,2,3,4,5])      
S = Solution()
# something = S.function(2)
something = S.function(0b00000010100101000001111010011100)
print(something)