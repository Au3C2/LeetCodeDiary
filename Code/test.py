'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2021-01-04 10:53:27
'''
import collections    
import heapq
from collections import deque
import functools
# from numba import njit
import numpy as np
import bisect

def function(n):
    f = [0,1,1]
    if n <= 2:
        return f[n]
    i = 3
    while i<=n:
        f[0]=f[1]
        f[1]=f[2]
        f[2]=f[0]+f[1]
        i+=1
    return f[-1]
something = function(4)
print(something)