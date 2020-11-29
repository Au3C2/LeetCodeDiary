'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2020-11-27 17:22:23
'''
import collections    
from collections import deque
    
def largestPerimeter(A: list) -> int:
    n = len(A)
    # max_L = 0
    A.sort(reverse=True)
    for i in range(n-2):
        L = A[i] + A[i+1] + A[i+2]
        if 2*A[i] < L:
            return L      
    return 0
    
something = largestPerimeter([3,2,3,4])
print(something)