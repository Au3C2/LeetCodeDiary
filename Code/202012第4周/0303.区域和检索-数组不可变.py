'''
Description: 
Autor: Au3C2
Date: 2020-12-23 15:02:05
LastEditors: Au3C2
LastEditTime: 2020-12-23 15:03:56
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.num_sum = [0,]
        for i in range(len(nums)):
            self.num_sum.append(self.num_sum[i]+nums[i])


    def sumRange(self, i: int, j: int) -> int:
        return self.num_sum[j+1] - self.num_sum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# 动态规划，简单题。这题和动态规划啥关系啊
# https://leetcode-cn.com/problems/range-sum-query-immutable/