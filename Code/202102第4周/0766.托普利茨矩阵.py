'''
Description: 
Autor: Au3C2
Date: 2021-02-22 10:54:40
LastEditors: Au3C2
LastEditTime: 2021-02-22 10:54:57
'''
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # m, n = len(matrix), len(matrix[0])
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True
# 数组，简单，每日一题
# https://leetcode-cn.com/problems/toeplitz-matrix/