'''
Description: 
Autor: Au3C2
Date: 2020-12-24 16:06:39
LastEditors: Au3C2
LastEditTime: 2020-12-24 16:07:14
'''
class Solution:
    def waysToStep(self, n: int) -> int:
        pre = [1,2,4]
        if n < 4:
            if n > 0:
                return pre[n-1]
            else:
                return 1
        for _ in range(3,n):
            res = (pre[0] + pre[1] + pre[2])%1000000007
            pre[0] = pre[1]
            pre[1] = pre[2]
            pre[2] = res
        return int(res)
# 动态简单题。中间过程也要取模，不然会超时呢
# https://leetcode-cn.com/problems/three-steps-problem-lcci/