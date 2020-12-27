'''
Description: 
Autor: Au3C2
Date: 2020-12-23 16:32:34
LastEditors: Au3C2
LastEditTime: 2020-12-23 16:34:02
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0]
        profit = 0
        for i in range(1, n):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
        return profit
# 动态规划，简单
# 0121.买卖股票的最佳时机的买卖多次版
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

