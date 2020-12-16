'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2020-12-16 09:03:27
'''
import collections    
import heapq
from collections import deque
import functools
# from numba import njit
import numpy as np
import bisect

def function(pattern: str, s: str):
    p_dict = {}
    w_dict = {}
    w_list = s.split(' ')
    if len(pattern) != len(w_list):
        return False
    for c,word in zip(pattern,s.split(' ')):
        if c not in p_dict:
            p_dict[c] = word
        elif p_dict[c] != word:
            return False
        
        if word not in w_dict:
            w_dict[word] = c
        elif w_dict[word] != c: 
            return False
    return True
something = function("aaa","aa aa aa aa")
print(something)