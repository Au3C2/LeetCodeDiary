'''
Description: 
Autor: Au3C2
Date: 2020-12-23 17:24:55
LastEditors: Au3C2
LastEditTime: 2020-12-23 17:25:27
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            # def maxProfit(self, prices: List[int]) -> int:
        buy_1 = buy_2 = float('inf') # 第一二次买之前的最低价
        pro_1 = pro_2 = 0
        
        for p in prices:
            buy_1 = min(buy_1, p)
            pro_1 = max(pro_1, p - buy_1)
            buy_2 = min(buy_2, p - pro_1) # p - pro_1 是用第一次的钱抵消了一部分第二次买的钱
            pro_2 = max(pro_2, p - buy_2)
        return pro_2

# 翻来覆去看几遍看不懂，溜了溜了
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/