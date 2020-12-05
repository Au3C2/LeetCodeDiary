'''
Description: 
Autor: Au3C2
Date: 2020-12-01 11:47:17
LastEditors: Au3C2
LastEditTime: 2020-12-01 11:47:27
'''
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        stack = [s]; ans = 0
        while stack:
            s = stack.pop()
            for c in set(s): # 遍历s中的唯一字母
                if s.count(c) < k:
                    temp = []
                    for t in s.split(c):
                        if t:
                            temp.append(t)
                    stack.extend(temp)
                    break
            else:
                ans = max(ans, len(s))
        return ans
