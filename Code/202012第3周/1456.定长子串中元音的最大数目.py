'''
Description: 
Autor: Au3C2
Date: 2020-12-16 15:41:48
LastEditors: Au3C2
LastEditTime: 2020-12-16 15:42:36
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        alphabet = 'aeiou'
        cur_count = 0
        for i in range(k):  #初始化长度为k的窗口
            if s[i] in alphabet:
                cur_count += 1
        if cur_count == k:
            return k
        max_count = cur_count
        for i in range(1,n-k+1): # 遍历查找
            # print(s[i-1],s[i+k-1])
            if s[i-1] in alphabet: 
                cur_count -= 1
            if s[i+k-1] in alphabet:
                cur_count += 1
            if cur_count == k:
                return k
            max_count = max(max_count,cur_count)
        return max_count

# 遍历查找。提交代码时忘记删掉print，时间竟然多了一倍，发现一个大秘密
# https://leetcode-cn.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/