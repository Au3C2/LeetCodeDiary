'''
Description: 
Autor: Au3C2
Date: 2020-12-23 09:21:28
LastEditors: Au3C2
LastEditTime: 2020-12-23 09:21:54
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_d = {}
        for i,c in enumerate(s):
            if c in s_d:
                s_d[c].append(i)
            else:
                s_d[c] = [i]
        min_idx = -1
        for c,idx in s_d.items():
            if len(idx) == 1:
                if min_idx == -1:
                    min_idx = idx[0]
                elif idx[0] < min_idx:
                    min_idx = idx[0]
        return min_idx
# 哈希表，简单题
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/