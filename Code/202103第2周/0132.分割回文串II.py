'''
Description: 
Autor: Au3C2
Date: 2021-03-08 10:41:07
LastEditors: Au3C2
LastEditTime: 2021-03-08 10:42:26
'''
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        g = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        f = [float("inf")] * n
        for i in range(n):
            if g[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if g[j + 1][i]:
                        f[i] = min(f[i], f[j] + 1)
        
        return f[n - 1]
    
# 动态规划，困难，改天好好看看
# https://leetcode-cn.com/problems/palindrome-partitioning-ii/