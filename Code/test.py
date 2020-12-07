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

def characterReplacement(numRows) -> int:
    if numRows == 0:
        return []
    output = [[1],[1,1]]
    if numRows == 1:
        return [[1]]
    for n in range(2,numRows): # 第n行,同时也是该行长度
        row = [1] # 这一行初始化
        for i in range(1,(n+1)//2+1): #因为是对称的仅需跑出一半的值
            row.append(output[n-1][i-1]+output[n-1][i])
        temp = row[:-1] if (n+1)%2==1 else row[:-2]
        row.extend(temp[::-1])
        output.append(row)
    return output
    
something = characterReplacement(1)
print(something)