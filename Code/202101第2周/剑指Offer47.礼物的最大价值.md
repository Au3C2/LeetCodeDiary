```python
'''
Description: 
Autor: Au3C2
Date: 2021-01-11 16:27:40
LastEditors: Au3C2
LastEditTime: 2021-01-11 16:28:08
'''
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0]*(n + 1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])+grid[i-1][j-1]
                
        return dp[m][n]      

# 动态规划，中等。感觉像是简单题
# https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/
```
