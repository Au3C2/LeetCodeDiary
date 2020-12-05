'''
Description: 
Autor: Au3C2
Date: 2020-12-03 12:28:52
LastEditors: Au3C2
LastEditTime: 2020-12-03 12:29:52
'''
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        if K >= n :
            return K
        if n == 0:
            return 0
        if sum(A) == 0:
            return K
        
        count = [0,0]
        lp = 0 #左指针
        max_len = K + 1
        cur_len = 0
        for rp in range(n): #右指针
            cur_len += 1
            count[A[rp]] += 1
            if cur_len > max_len and count[1] + K >= cur_len:
                max_len = cur_len
            if count[1] + K < cur_len:
                count[A[lp]] -= 1
                lp += 1
                cur_len -= 1
        return max_len
        
# 这道题是 No.0424 的简化