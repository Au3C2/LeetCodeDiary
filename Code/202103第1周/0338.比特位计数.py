'''
Description: 
Autor: Au3C2
Date: 2021-03-03 10:31:00
LastEditors: Au3C2
LastEditTime: 2021-03-03 10:31:56
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        for n in range(1,num+1):
            ans.append(ans[n//2]+n%2)
        return ans
    
# 动态规划，中等，每日一题
# 做过的
# https://leetcode-cn.com/problems/counting-bits/