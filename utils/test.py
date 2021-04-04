'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-04-03 19:13:50
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
        square = [1]
        i = 1
        while True:
            if i **2 < n:
                square.append(i**2)
                i += 1
            elif i ** 2 == n:
                return 1
            else:
                break
        t = i-1
        dp = [0]*(n+1)
        j = 1
        for i in range(1,n+1):
            if j +1 <= t  and square[j+1] <= i:
                j += 1  
            mindp = dp[i-square[j]]
            for k in range(j,0,-1):
                mindp = min(dp[i-square[k]],mindp)
            dp[i] = mindp + 1
        return dp[n]

            

null = None
# root = buildTree([-10,9,20,null,null,15,7])
# t2 = buildTree([2,1,3,null,4,null,7])      
# head = buildList([1,2,3,4,5])      
S = Solution()
# something = S.function(2)
something = S.function(48)
print(something)