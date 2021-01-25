'''
Description: 
Autor: Au3C2
Date: 2021-01-25 16:08:47
LastEditors: Au3C2
LastEditTime: 2021-01-25 16:09:04
'''
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1
        t = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                # print(nums[i])
                t += 1
            else:
                ans = max(ans,t)
                t = 1
        return max(ans,t)
# 数组，简单，每日一题
# https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/