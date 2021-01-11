'''
Description: 
Autor: Au3C2
Date: 2021-01-08 11:08:41
LastEditors: Au3C2
LastEditTime: 2021-01-08 11:09:35
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:]+nums[:-k]

# 数组，中等。简单有趣的一题。
# 原来python列表的复制还蛮多学问的
# https://leetcode-cn.com/problems/rotate-array/