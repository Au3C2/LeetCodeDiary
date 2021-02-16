'''
Description: 
Autor: Au3C2
Date: 2021-02-16 11:54:14
LastEditors: Au3C2
LastEditTime: 2021-02-16 11:54:41
'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
    
# 数组，简单，每日一题
# 竟然写的和答案一毛一样
# https://leetcode-cn.com/problems/array-partition-i/