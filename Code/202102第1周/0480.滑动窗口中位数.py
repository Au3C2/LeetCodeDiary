'''
Description: 
Autor: Au3C2
Date: 2021-02-04 11:14:39
LastEditors: Au3C2
LastEditTime: 2021-02-04 11:15:09
'''
import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        median = lambda a: (a[(len(a)-1)//2] + a[len(a)//2]) / 2
        a = sorted(nums[:k])
        res = [median(a)]
        for i, j in zip(nums[:-k], nums[k:]):
            a.pop(bisect.bisect_left(a, i))
            a.insert(bisect.bisect_left(a, j), j)
            res.append(median(a))
        return res
    
# 滑动窗口，困难，每日一题。抄的
# https://leetcode-cn.com/problems/sliding-window-median/