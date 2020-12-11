'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2020-12-10 09:16:26
'''
import collections    
import heapq
from collections import deque
import functools
# from numba import njit
import numpy as np

def characterReplacement(bills) -> bool:
    change5, change10 = 0,0
    for num in bills:
        if num ==5:
            change5 += 1
        if num == 10:
            if change5 > 0:
                change5 -= 1
                change10 += 1
            else:
                return False
        if num == 20:
            if (change5>0 and change10>0):
                change10 -= 1
                change5 -= 1
            elif change5 >= 3:
                change5 -= 3
            else:
                return False
    return True
    
something = characterReplacement([5,5,10,10,20])
print(something)