'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2020-12-04 14:52:27
'''
import collections    
import heapq
from collections import deque
import functools
# from numba import njit
import numpy as np

def characterReplacement(stones) -> int:
    stones.sort()
    n = len(stones)
    #最大值
    maxs = stones[n-1]-stones[0]+1-n- \
        min(stones[n-1]-stones[n-2]-1,stones[1]-stones[0]-1)
    #最小值
    mins = maxs
    tmp = 0
    for i in range(n):
        while stones[i]-stones[tmp]+1>n:
            tmp += 1
        cost = n-(i-tmp+1)
        if cost == 1 and \
            stones[i]-stones[tmp]+1 == n-1: # 左端致密情况
            mins = min(mins,2)
        else:
            mins = min(mins,cost) # 一般情况
    return [mins,maxs]
    
something = characterReplacement([6,5,4,3,10])
print(something)