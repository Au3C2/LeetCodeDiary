'''
Description: 
Autor: Au3C2
Date: 2020-12-31 10:42:34
LastEditors: Au3C2
LastEditTime: 2021-01-04 11:11:45
'''
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        square = []
        i = 1
        while True:
            if i **2 <= n:
                square.append(i**2)
                i += 1
            else:
                break
        # j = 0
        dp = [False]*(n+1)
        for i in range(1,n+1):
            j = 0
            while square[j] <= i:
                if dp[i-square[j]]:# 下一步Bob的情况为True
                    j += 1
                    if j==len(square):
                        break
                else: # 下一步Bob的情况为False
                    dp[i] = True
                    break
        return dp[n]

# 动态规划，困难。但是做起来比前面几个石子简单
# https://leetcode-cn.com/problems/stone-game-iv/