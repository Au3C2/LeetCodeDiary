'''
Description: 
Autor: Au3C2
Date: 2021-01-04 10:54:08
LastEditors: Au3C2
LastEditTime: 2021-01-04 10:54:42
'''
class Solution:
    def fib(self, n: int) -> int:
        f = [0,1,1]
        if n <= 2:
            return f[n]
        i = 3
        while i<=n:
            f[0]=f[1]
            f[1]=f[2]
            f[2]=f[0]+f[1]
            i+=1
        return f[-1]

# 数组，简单题，斐波那契额数列
# https://leetcode-cn.com/problems/fibonacci-number/