'''
Description: 
Autor: Au3C2
Date: 2021-01-14 15:01:00
LastEditors: Au3C2
LastEditTime: 2021-01-14 15:02:10
'''
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        num = 0
        ans = []
        for a in A:
            num = ((num<<1) + a)%5
            ans.append(not num)
        return ans

# 数组，简单，每日一题，有意思
# https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/