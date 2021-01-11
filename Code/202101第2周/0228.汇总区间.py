'''
Description: 
Autor: Au3C2
Date: 2021-01-10 11:19:40
LastEditors: Au3C2
LastEditTime: 2021-01-10 11:19:55
'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        n = len(nums)
        if n ==1 :
            return [str(nums[0])]
        ans = []
        i = 0
        while i<n:
            j = i+1  

            while j<n and nums[j]-nums[j-1] == 1:
                j += 1
                
            if j-1 == i:
                ans.append('%d'%(nums[i]))
            else:
                ans.append('%d->%d'%(nums[i],nums[j-1]))
            i = j
        return ans

# 数组，简单，每日一题
# https://leetcode-cn.com/problems/summary-ranges/