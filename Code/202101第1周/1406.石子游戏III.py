'''
Description: 
Autor: Au3C2
Date: 2021-01-06 16:10:34
LastEditors: Au3C2
LastEditTime: 2021-01-06 16:11:30
'''
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            temp = []
            j = 0
            while j < 3 and i+j<n:
                temp.append(sum(stoneValue[i:i+j+1])-dp[i+j+1])
                j += 1
            dp[i] = max(temp)
        if dp[0] > 0:
            return 'Alice'
        if dp[0] == 0:
            return 'Tie'
        if dp[0] < 0:
            return 'Bob'
# 动态规划，困难。可以进一步优化空间复杂度至O(1)
# 想清楚后感觉不太难
# https://leetcode-cn.com/problems/stone-game-iii/