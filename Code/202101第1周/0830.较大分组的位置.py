'''
Description: 
Autor: Au3C2
Date: 2021-01-05 11:57:03
LastEditors: Au3C2
LastEditTime: 2021-01-05 11:57:40
'''
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        start, end = 0, 1
        while end < len(s):
            while end < len(s) and s[end] == s[start]:
                end += 1
            if end-start >= 3:
                res.append([start,end-1])
            start = end
            end = start +1
        return res

# 数组，简单。有滑动窗口那味了
# https://leetcode-cn.com/problems/positions-of-large-groups/