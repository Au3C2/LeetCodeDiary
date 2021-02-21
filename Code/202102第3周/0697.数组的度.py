'''
Description: 
Autor: Au3C2
Date: 2021-02-20 13:58:39
LastEditors: Au3C2
LastEditTime: 2021-02-20 13:59:00
'''
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = {}
        max_count = 0
        max_num = None
        for i,n in enumerate(nums):
            if n in counter:
                counter[n][0] += 1
                counter[n][2] = i
            else:
                counter[n] = [1,i,i]
        for count in counter.values():
            if count[0] > max_count:
                res = count[2] - count[1]
                max_count = count[0]
            elif count[0] == max_count:
                res = min(count[2] - count[1],res)            
        
        return res+1
# 数组，简单，每日一题
# https://leetcode-cn.com/problems/degree-of-an-array/