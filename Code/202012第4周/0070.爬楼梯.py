'''
Description: 
Autor: Au3C2
Date: 2020-12-24 11:40:45
LastEditors: Au3C2
LastEditTime: 2020-12-24 15:01:59
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        pre = [1,2]
        if n < 3:
            if n > 0:
                return pre[n-1]
            else:
                return 1
        for _ in range(2,n):
            res = pre[0] + pre[1]
            pre[0] = pre[1]
            pre[1] = res
        return res
# 动态规划,简单
# https://leetcode-cn.com/problems/climbing-stairs/