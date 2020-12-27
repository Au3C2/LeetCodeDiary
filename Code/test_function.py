'''
Description: 
Autor: Au3C2
Date: 2020-12-23 12:38:40
LastEditors: Au3C2
LastEditTime: 2020-12-23 12:46:32
'''
class NumArray:
    def __init__(self, nums):
        import numpy as np
        self.nums = np.array(nums[0])
    def sumRange(self, i: int, j: int) -> int:
        import numpy as np
        return int(np.sum(self.nums[i:j+1]))

obj = NumArray([[-2,0,3,-5,2,-1]])
param_1 = obj.sumRange(0,2)
pass