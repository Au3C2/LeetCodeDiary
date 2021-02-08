'''
Description: 
Autor: Au3C2
Date: 2021-02-05 10:33:55
LastEditors: Au3C2
LastEditTime: 2021-02-05 10:34:22
'''
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n=len(s)
        j=-1
        for i in range(n):
            maxCost -= (abs(ord(s[i])-ord(t[i])))
            if maxCost < 0:
                j +=1
                maxCost += (abs(ord(s[j])-ord(t[j])))
        return n-1-j
    
# 滑动窗口，中等，每日一题，做过了喜喜
# https://leetcode-cn.com/problems/get-equal-substrings-within-budget/