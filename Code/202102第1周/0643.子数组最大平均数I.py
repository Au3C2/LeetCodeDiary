'''
Description: 
Autor: Au3C2
Date: 2021-02-04 11:13:06
LastEditors: Au3C2
LastEditTime: 2021-02-04 11:13:30
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumk = sum(nums[:k])
        ans = sumk
        for i in range(k,len(nums)):
            sumk = sumk - nums[i-k] + nums[i]
            ans = max(sumk,ans)
        return ans/k
    
# 数组，简单，每日一题。像是滑动窗口
# https://leetcode-cn.com/problems/maximum-average-subarray-i/