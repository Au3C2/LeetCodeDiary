'''
Description: 
Autor: Au3C2
Date: 2021-02-24 11:18:39
LastEditors: Au3C2
LastEditTime: 2021-02-24 11:18:58
'''
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        ans = [[0] *n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = 1-A[i][n-j-1]
        return ans
    
# 数组，简单，每日一题
# https://leetcode-cn.com/problems/flipping-an-image/