'''
Description: 
Autor: Au3C2
Date: 2020-12-25 11:42:11
LastEditors: Au3C2
LastEditTime: 2020-12-25 11:42:41
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        for n in range(1,num+1):
            ans.append(ans[n//2]+n%2)
        return ans
# 动态规划，中等，挺有意思的
# https://leetcode-cn.com/problems/counting-bits/