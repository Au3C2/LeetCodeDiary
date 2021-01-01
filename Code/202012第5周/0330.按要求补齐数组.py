'''
Description: 
Autor: Au3C2
Date: 2020-12-29 09:28:13
LastEditors: Au3C2
LastEditTime: 2020-12-29 09:37:32
'''
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, x = 0, 1
        length, index = len(nums), 0

        while x <= n:
            if index < length and nums[index] <= x:
                x += nums[index]
                index += 1
            else:
                x <<= 1 # 左移1位，相当于乘2了
                patches += 1
        
        return patches
# 贪心，困难，每日一题
# 数学+编程，数学推理的多一些
# https://leetcode-cn.com/problems/patching-array/solution/an-yao-qiu-bu-qi-shu-zu-by-leetcode-solu-klp1/