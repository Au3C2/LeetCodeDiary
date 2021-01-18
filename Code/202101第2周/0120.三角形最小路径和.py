'''
Description: 
Autor: Au3C2
Date: 2021-01-11 16:53:21
LastEditors: Au3C2
LastEditTime: 2021-01-11 16:55:05
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[0]*(i) for i in range(1,m+1)]
        dp[0][0] = triangle[0][0]
        
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][-1] = dp[i-1][-1] + triangle[i][-1]
        for i in range(2,m):
            for j in range(1,i):
                dp[i][j] = min(dp[i-1][j],dp[i-1][j-1]) + triangle[i][j]        

        return min(dp[m-1])

# 动态规划，中等。还能继续优化空间复杂度。因为在计算这一行的结果时，只需要上一行的信息，
# 因此只需要1个长度为n-1的数组即可。但是我懒
# https://leetcode-cn.com/problems/triangle/