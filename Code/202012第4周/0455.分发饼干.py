'''
Description: 
Autor: Au3C2
Date: 2020-12-25 09:39:53
LastEditors: Au3C2
LastEditTime: 2020-12-25 09:47:15
'''
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        counter=0
        while g and s:
            if g[0]<=s[0]:
                s.pop(0)
                g.pop(0)
                counter+=1
            else:
                s.pop(0)
        return counter

# 圣诞快乐！贪心简单题，分饼干啦
# https://leetcode-cn.com/problems/assign-cookies/