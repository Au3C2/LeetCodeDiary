'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2020-12-25 17:32:38
'''
import collections    
import heapq
from collections import deque
import functools
# from numba import njit
import numpy as np
import bisect

def function(s,t):     
    s2t = {}
    t2s = {}
    for sc, tc in zip(s,t):
        if sc in s2t and s2t[sc] != tc:
            return False
        else:
            s2t[sc] = tc
        if tc in t2s and t2s[tc] != sc:
            return False          
        else:
            t2s[tc] = sc
    for sc,tc in s2t.items():
        if t2s[tc] != sc:
            return False
    for tc,sc in t2s.items():
        if s2t[sc] != tc:
            return False
    return True
something = function("egg","add")
print(something)