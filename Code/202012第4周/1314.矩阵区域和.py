'''
Description: 
Autor: Au3C2
Date: 2020-12-25 16:36:11
LastEditors: Au3C2
LastEditTime: 2020-12-25 16:37:04
'''
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        cum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                cum[i][j] = cum[i-1][j] + cum[i][j-1] - cum[i-1][j-1] + mat[i-1][j-1]
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x1 = i-K+1 if i-K > 0 else 1
                x2 = i+K+1 if i+K < m else m
                y1 = j-K+1 if j-K > 0 else 1
                y2 = j+K+1 if j+K < n else n
                ans[i][j] = cum[x2][y2] - cum[x2][y1-1] - cum[x1-1][y2] + cum[x1-1][y1-1]
        return ans
# 动态规划,中等
# 同样的代码，改成numpy，内存的和时间双双翻倍
# https://leetcode-cn.com/problems/matrix-block-sum/