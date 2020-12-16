'''
Description: 
Autor: Au3C2
Date: 2020-12-16 09:05:17
LastEditors: Au3C2
LastEditTime: 2020-12-16 09:06:01
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_dict = {}
        w_dict = {}
        w_list = s.split(' ')
        if len(pattern) != len(w_list):
            return False
        for c,word in zip(pattern,s.split(' ')):
            if c not in p_dict:
                p_dict[c] = word
            elif p_dict[c] != word:
                return False
            
            if word not in w_dict:
                w_dict[word] = c
            elif w_dict[word] != c: 
                return False
        return True
# 哈希表，简单题，在两个字符串之间建立双射即可
# https://leetcode-cn.com/problems/word-pattern/
