'''
Description: 
Autor: Au3C2
Date: 2021-02-23 10:58:59
LastEditors: Au3C2
LastEditTime: 2021-02-23 10:59:59
'''
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        import numpy as np
        n = len(customers)
        grumpy = np.array(grumpy,dtype=np.uint8)
        max_customers = min_customers = np.sum(customers*(1-grumpy))
        
        if n<=X or sum(grumpy)==0:
            return sum(customers)

        customers = customers*grumpy
        for i in range(n+1-X):
            now_customers = np.sum(customers[i:i+X])+min_customers
            max_customers = max(max_customers,now_customers)
        return max_customers
    
# 贪心算法，中等，每日一题
# https://leetcode-cn.com/problems/grumpy-bookstore-owner/