'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2020-12-29 12:13:36
'''
import collections    
import heapq
from collections import deque
import functools
# from numba import njit
import numpy as np
import bisect

def function(piles):
    length = len(piles)
    sum_piles = 0
    dp = [[0] * (length+1) for _ in range(length)]
    for i in range(length-1,-1,-1):
        sum_piles += piles[i]
        for m in range(1,length+1):
            if i+2*m >= length:
                dp[i][m] = sum_piles
            else:
                for x in range(1,2*m+1):
                    dp[i][m] = max(dp[i][m],sum_piles-dp[i+x][max(m,x)])
    return dp[0][1]        
something = function([2,7,9,4,4])
print(something)