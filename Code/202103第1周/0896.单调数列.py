'''
Description: 
Autor: Au3C2
Date: 2021-02-28 14:09:57
LastEditors: Au3C2
LastEditTime: 2021-02-28 14:10:18
'''
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 3:
            return True
        
        lastDiff = None
        
        for i in range(1,len(A)):
            thisDiff = A[i] - A[i-1]
            if thisDiff == 0:
                continue
            if thisDiff > 0 :
                if lastDiff and lastDiff < 0:
                    return False
            if thisDiff < 0 :
                if lastDiff and lastDiff > 0:
                    return False
            lastDiff = thisDiff
        return True
# 数组，简单，每日一题
# https://leetcode-cn.com/problems/monotonic-array/