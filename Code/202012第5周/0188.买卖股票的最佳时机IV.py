'''
Description: 
Autor: Au3C2
Date: 2020-12-28 10:37:19
LastEditors: Au3C2
LastEditTime: 2020-12-28 10:37:48
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not k: return 0     
        buy = [float('inf')] *k # 第一二次买之前的最低价
        pro = [0] * k
        for p in prices:
            buy[0] = min(buy[0], p)
            pro[0] = max(pro[0], p - buy[0])
            for i in range(1,k):
                buy[i] = min(buy[i], p-pro[i-1])
                pro[i] = max(pro[i], p-buy[i])
        return pro[-1]
# 动态规划，困难
# 买股票终极版
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/
