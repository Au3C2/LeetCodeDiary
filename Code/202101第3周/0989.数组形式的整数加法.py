'''
Description: 
Autor: Au3C2
Date: 2021-01-22 09:51:47
LastEditors: Au3C2
LastEditTime: 2021-01-22 09:52:06
'''
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        ans = 0
        p = 0
        i = -1
        n = len(A)
        while K or p:
            if -i <= n:
                t = A[i] + K%10 + p
                A[i] = t % 10
                p = t // 10
            elif -i > n:
                A.insert(0,(K%10+p)%10)
                p = (K%10 + p)//10
            i -= 1
            K = K//10
        return A
# 数组，简单，每日一题
# https://leetcode-cn.com/problems/add-to-array-form-of-integer/