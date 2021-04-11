'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-04-10 10:58:26
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
        pass
        
    def function(self,n):
        n = abs(n)
        while n > 0:
            if n == 1:
                return True
            elif n % 2 == 0:
                n = n//2
            elif n % 3 == 0:
                n = n//3
            elif n % 5 == 0:
                n = n//5
            else:
                return False
        return True        

null = None
# root = buildTree([-10,9,20,null,null,15,7])
# t2 = buildTree([2,1,3,null,4,null,7])      
# head = buildList([1,2,3,4,5])      
S = Solution()
# something = S.function(2)
# something = S.function(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
something = S.function(-2147483648)
print(something)