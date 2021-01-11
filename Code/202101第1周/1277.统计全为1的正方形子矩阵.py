'''
Description: 
Autor: Au3C2
Date: 2021-01-08 11:10:15
LastEditors: Au3C2
LastEditTime: 2021-01-08 16:17:47
'''
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                cum[i][j] = cum[i-1][j] + cum[i][j-1] - cum[i-1][j-1] + matrix[i-1][j-1]
        ans = 0
        # for w in range(min(m,n)):
        # fullArea = (w+1)**2
        fullArea = [i**2 for i in range(1,min(m,n)+1)]
        i = 1
        while i <= m:
            j = 1
            while j <= n:
                w = 0
                while i+w<=m and j+w<=n:
                    area = cum[i+w][j+w] - cum[i+w][j-1] - cum[i-1][j+w] + cum[i-1][j-1]
                    if area == fullArea[w]:
                        ans += 1
                    else:
                        break
                    w += 1
                j +=1
            i += 1
                
        return ans
# 动态规划,中等。先求前缀和，再遍历查找
# https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        f = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    f[i][j] = 0
                else:
                    f[i][j] = min(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1]) + 1
                ans += f[i][j]
        return ans

# 正常动态规划求法
