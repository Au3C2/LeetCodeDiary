'''
Description: 
Autor: Au3C2
Date: 2020-12-31 10:01:55
LastEditors: Au3C2
LastEditTime: 2020-12-31 10:02:23
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        right = intervals[0][1]
        ans = 1

        for i in range(1, n):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]
        
        return n - ans

# 贪心，中等，每日一题
# https://leetcode-cn.com/problems/non-overlapping-intervals/