'''
Description: 
Autor: Au3C2
Date: 2021-02-25 12:07:26
LastEditors: Au3C2
LastEditTime: 2021-02-25 12:07:35
'''
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = [[0] *m for _ in range(n)]
        
        for i in range(0,m):
            for j in range(0,n):
                ans[j][i] = matrix[i][j]
        return ans
    
# 数组，简单，每日一题
# https://leetcode-cn.com/problems/transpose-matrix/