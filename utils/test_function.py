'''
Description: 
Autor: Au3C2
Date: 2020-12-23 12:38:40
LastEditors: Au3C2
LastEditTime: 2021-03-02 11:32:24
'''
class NumArray:
    def __init__(self, matrix):
        self.m, self.n = len(matrix), len(matrix[0])
        self.num_sum = [[0]*(self.n+1) for _ in range(self.m+1)]
        for i in range(1,self.m+1):
            for j in range(1,self.n+1):
                self.num_sum[i][j] = self.num_sum[i-1][j] + self.num_sum[i][j-1] - self.num_sum[i-1][j-1] + matrix[i-1][j-1]
                
    def sumRange(self, row1,col1,row2,col2) -> int:
        return self.num_sum[row2+1][col2+1] - self.num_sum[row2+1][col1] - self.num_sum[row1][col2+1] + self.num_sum[row1][col1]

obj = NumArray([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])
param_1 = obj.sumRange(1, 2, 2, 4)
pass