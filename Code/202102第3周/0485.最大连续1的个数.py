'''
Description: 
Autor: Au3C2
Date: 2021-02-15 14:12:44
LastEditors: Au3C2
LastEditTime: 2021-02-15 14:13:01
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        res = 0
        for n in nums:
            if n:
                counter += 1
            else:
                res = max(counter,res)
                counter = 0
        return max(counter,res)
    
# 数组，简单，每日一题
# https://leetcode-cn.com/problems/max-consecutive-ones/