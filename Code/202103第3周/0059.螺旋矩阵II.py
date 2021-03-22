'''
Description: 
Autor: Au3C2
Date: 2021-03-22 16:47:58
LastEditors: Au3C2
LastEditTime: 2021-03-22 16:48:44
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        direc = [[0,1],[1,0],[0,-1],[-1,0]]
        bound = [1,0,n-1,n-1] # 上左下右边界
        d = 0
        x = 0
        y = 0
        i = 1
        while 1:
            matrix[x][y] = i
            i += 1
            if i == n*n+1:
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
            
        return matrix

# 矩阵，中等
# https://leetcode-cn.com/problems/spiral-matrix-ii/