'''
Description: 
Autor: Au3C2
Date: 2020-12-21 15:47:15
LastEditors: Au3C2
LastEditTime: 2020-12-23 09:08:09
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev = curr = 0
        for i in range(2, n + 1):
            nxt = min(curr + cost[i - 1], prev + cost[i - 2])
            prev, curr = curr, nxt
        return curr

# 动态规划简单题，不会
# https://leetcode-cn.com/problems/min-cost-climbing-stairs/