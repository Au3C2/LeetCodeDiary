'''
Description: 
Autor: Au3C2
Date: 2021-03-17 12:12:27
LastEditors: Au3C2
LastEditTime: 2021-03-17 15:15:40
'''
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)

        dp = [1] + [0] * n

        for i in range(1, m + 1):
            for j in range(min(i,n), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[-1]

# 动态规划，困难，每日一题。动态规划还是不太会，准备重回动态规划
# https://leetcode-cn.com/problems/distinct-subsequences/