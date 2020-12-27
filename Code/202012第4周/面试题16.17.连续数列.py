'''
Description: 
Autor: Au3C2
Date: 2020-12-24 09:57:35
LastEditors: Au3C2
LastEditTime: 2020-12-24 09:59:05
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        ans = nums[0]
        for n in nums:
            pre = max(pre+n,n)
            ans = max(ans,pre)
        return ans
# 动态规划简单题, 与0053.最大子序和 相同
# https://leetcode-cn.com/problems/contiguous-sequence-lcci/