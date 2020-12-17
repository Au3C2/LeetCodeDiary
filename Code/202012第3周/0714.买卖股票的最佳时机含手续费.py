'''
Description: 
Autor: Au3C2
Date: 2020-12-17 16:25:45
LastEditors: Au3C2
LastEditTime: 2020-12-17 16:26:32
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = prices[0] + fee
        profit = 0
        for i in range(1, n):
            if prices[i] + fee < buy:
                buy = prices[i] + fee
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
        return profit
    
# 每日一题，贪心、动态规划，不会
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-han-sh-rzlz/