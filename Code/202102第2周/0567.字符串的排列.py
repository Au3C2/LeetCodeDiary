'''
Description:
Autor: Au3C2
Date: 2021-02-10 10:54:18
LastEditors: Au3C2
LastEditTime: 2021-02-10 10:55:09
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = collections.Counter(s1)
        l_s1, l_s2 = len(s1), len(s2)
        if l_s1 > l_s2 :
            return False
        count_t = collections.Counter(s2[0:l_s1])
        # end = (l_s2-l_s1) if l_s2-l_s1 > 1 else 2
        for i in range(l_s2-l_s1+1):
            flag = True
            for c, n in count_s1.items():
                if count_t[c] == n:
                    continue
                else:
                    flag = False
                    break
            if flag:
                return True
            if i == l_s2-l_s1:
                break
            count_t[s2[i]] -= 1
            count_t[s2[i+l_s1]] += 1
            lookup = s2[i:i+l_s1] 
        return False
    
# 滑动窗口，中等，但我用的哈希表解法？
# https://leetcode-cn.com/problems/permutation-in-string/
    