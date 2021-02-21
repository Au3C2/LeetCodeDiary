'''
Description: 
Autor: Au3C2
Date: 2021-02-17 10:36:56
LastEditors: Au3C2
LastEditTime: 2021-02-17 10:37:24
'''
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        ro, co = len(nums), len(nums[0])
        if ro*co != r*c:
            return nums
        ans = [[0]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                ans[i][j] = nums[(i*c+j)//co][(i*c+j)%co]
        return ans
    
# 数组，简单，每日一题
# https://leetcode-cn.com/submissions/detail/146201623/