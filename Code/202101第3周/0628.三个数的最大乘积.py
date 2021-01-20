'''
Description: 
Autor: Au3C2
Date: 2021-01-20 10:07:11
LastEditors: Au3C2
LastEditTime: 2021-01-20 10:07:37
'''
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        nums.sort()    
        # if nums[1] < 0 :
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])

# 数组，简单，每日一题
# https://leetcode-cn.com/problems/maximum-product-of-three-numbers/