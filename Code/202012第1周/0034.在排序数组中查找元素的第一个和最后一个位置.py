'''
Description: 
Autor: Au3C2
Date: 2020-12-01 08:45:30
LastEditors: Au3C2
LastEditTime: 2020-12-01 08:45:43
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        if target not in nums:
            return [-1,-1]
        begin, end = l, 0
        isbegin, isend = True, True
        for i in range(l):
            if nums[i] == target and isbegin:
                isbegin = False
                begin = i
            if nums[-(i+1)] == target and isend:
                end = l-i-1
                isend = False
            if not isbegin and not isend: 
                break

        return [begin,end]
