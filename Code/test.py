'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2020-12-31 10:14:54
'''
import collections    
import heapq
from collections import deque
import functools
# from numba import njit
import numpy as np
import bisect

def function(flowerbed, n):
    if n == 0:
        return True
    if len(flowerbed) == 1:
        if flowerbed[0] == 1:
            return False
        else:
            return True
    
    if flowerbed[0]+flowerbed[1] == 0:
        flowerbed[0] = 1
        n -= 1
    if flowerbed[-1]+flowerbed[-2] == 0:
        flowerbed[-1] = 1
        n -= 1
        
    for i in range(1,len(flowerbed)-2):
        if flowerbed[i-1]+flowerbed[i]+flowerbed[i+1]==0:
            flowerbed[i] = 1
            n -= 1

    return n <= 0
something = function(flowerbed = [0,0,1,0,0], n = 1)
print(something)