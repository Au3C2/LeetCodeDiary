'''
Description: 
Autor: Au3C2
Date: 2020-12-24 15:14:57
LastEditors: Au3C2
LastEditTime: 2020-12-24 15:15:26
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            if n == 3:
                return max(nums[0]+nums[2],nums[1])
            elif n == 2 or n == 1:
                return max(nums)
            elif n == 0:
                return 0
        pre3, pre2 = nums[0], nums[1]
        pre1 = pre3 + nums[2]
        for i in range(3,n):
            cur = nums[i] + max(pre2,pre3)
            pre3 = pre2
            pre2 = pre1
            pre1 = cur
        return max(pre2,cur)
# 同 面试题 17.16. 按摩师 ，动态规划，简单
# https://leetcode-cn.com/problems/house-robber/