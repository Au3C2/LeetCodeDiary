'''
Description: 
Autor: Au3C2
Date: 2021-03-02 11:35:53
LastEditors: Au3C2
LastEditTime: 2021-03-02 11:36:29
'''
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return None
        self.m, self.n = len(matrix), len(matrix[0])
        self.num_sum = [[0]*(self.n+1) for _ in range(self.m+1)]
        for i in range(1,self.m+1):
            for j in range(1,self.n+1):
                self.num_sum[i][j] = self.num_sum[i-1][j] + self.num_sum[i][j-1] - self.num_sum[i-1][j-1] + matrix[i-1][j-1]
              

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.num_sum[row2+1][col2+1] - self.num_sum[row2+1][col1] - self.num_sum[row1][col2+1] + self.num_sum[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# 数组，中等，每日一题。0303的二维版
# https://leetcode-cn.com/problems/range-sum-query-2d-immutable/