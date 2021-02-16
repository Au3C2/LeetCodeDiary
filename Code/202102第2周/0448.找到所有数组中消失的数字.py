'''
Description: 
Autor: Au3C2
Date: 2021-02-13 11:56:55
LastEditors: Au3C2
LastEditTime: 2021-02-13 11:58:59
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for n in nums:
            nums[(n-1)%l] += l
        ans = list()
        for i,n in enumerate(nums):
            if n <= l:
                ans.append(i+1)
        return ans
    
    
# 数组，简单，每日一题。仔细想想原地修改的办法还是不错的
# https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/