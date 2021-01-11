'''
Description: 
Autor: Au3C2
Date: 2021-01-08 16:30:29
LastEditors: Au3C2
LastEditTime: 2021-01-08 16:31:12
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        f = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '0':
                    f[i][j] = 0
                else:
                    f[i][j] = min(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1]) + 1
                ans = max(ans,f[i][j])
        return ans**2

# 动态规划，中等。与1227解法类似
# https://leetcode-cn.com/problems/maximal-square/