'''
Description: 
Autor: Au3C2
Date: 2021-03-06 11:31:46
LastEditors: Au3C2
LastEditTime: 2021-03-06 11:32:17
'''
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = list()
        l_nums = len(nums)
        for i,n in enumerate(nums):
            j = (i+1) % l_nums
            while nums[j]<=n:
                j = (j+1) % l_nums
                if j == i:
                    break
            if j == i:
                ans.append(-1)
            else:
                ans.append(nums[j])
        return ans
    
# 栈，中等，每日一题。结果我用遍历搜索过了
# https://leetcode-cn.com/problems/next-greater-element-ii/