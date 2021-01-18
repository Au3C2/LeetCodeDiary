'''
Description: 
Autor: Au3C2
Date: 2021-01-11 16:38:35
LastEditors: Au3C2
LastEditTime: 2021-01-11 16:39:12
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0]*(n) for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]        

        return dp[m-1][n-1]     

# 动态规划，中等,和`剑指Offer47.礼物的最大价值`差不多
# https://leetcode-cn.com/problems/minimum-path-sum/