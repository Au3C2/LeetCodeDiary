'''
Description: 
Autor: Au3C2
Date: 2021-02-08 10:36:07
LastEditors: Au3C2
LastEditTime: 2021-02-08 10:36:34
'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if changed: 
                    return False
                changed = True
                
                # 修改num[i]会导致nums[i-1] > nums[i]
                if i > 0 and nums[i-1] > nums[i+1]: 
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
        return True
    
# 数组，简单。简单但是不好做
# https://leetcode-cn.com/problems/non-decreasing-array/