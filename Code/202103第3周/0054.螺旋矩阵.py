'''
Description: 
Autor: Au3C2
Date: 2021-03-15 12:46:20
LastEditors: Au3C2
LastEditTime: 2021-03-15 12:46:47
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        direc = [[0,1],[1,0],[0,-1],[-1,0]]
        bound = [1,0,m-1,n-1] # 上左下右边界
        res = list()
        d = 0
        x = 0
        y = 0
        i = 0
        while 1:
            res.append(matrix[x][y])
            i += 1
            if i == m*n:
                break

            if direc[d][0] == 1 and x == bound[2]: #向下移动碰到边界
                d = (d+1)%4
                bound[2] -= 1
            if direc[d][0] == -1 and x == bound[0]:#向上移动碰到边界
                d = (d+1)%4
                bound[0] += 1

            if direc[d][1] == 1 and y == bound[3]:#向右移动碰到边界
                d = (d+1)%4
                bound[3] -= 1    
            if direc[d][1] == -1 and y == bound[1]:#向左移动碰到边界
                d = (d+1)%4
                bound[1] += 1

            x += direc[d][0]
            y += direc[d][1]
            
        return res
# 数组，中等
# https://leetcode-cn.com/problems/spiral-matrix/