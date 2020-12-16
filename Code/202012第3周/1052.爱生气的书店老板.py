'''
Description: 
Autor: Au3C2
Date: 2020-12-14 13:10:09
LastEditors: Au3C2
LastEditTime: 2020-12-14 13:10:45
'''
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        min_customers = 0
        if n<=X or sum(grumpy)==0:
            return sum(customers)
        for i in range(n):
            min_customers += (1-grumpy[i])*customers[i]
            customers[i] = customers[i]*grumpy[i]    
        max_customers = min_customers    
        for i in range(n+1-X):
            now_customers = sum(customers[i:i+X])+min_customers
            max_customers = max(max_customers,now_customers)
        return max_customers

# https://leetcode-cn.com/problems/grumpy-bookstore-owner/
# 滑窗，难度一般
