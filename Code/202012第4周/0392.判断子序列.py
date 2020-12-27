'''
Description: 
Autor: Au3C2
Date: 2020-12-24 15:38:02
LastEditors: Au3C2
LastEditTime: 2020-12-24 15:47:05
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        i = 0
        n_s = len(s)
        for c in t:
            if c == s[i]:
                i += 1
            if i == n_s:
                break
        return i == n_s
# 简单题，这是动态规划？
# 可以用，但是针对大量s个数时，才能省时间
# https://leetcode-cn.com/problems/is-subsequence/