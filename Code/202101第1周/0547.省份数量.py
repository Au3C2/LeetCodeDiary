'''
Description: 
Autor: Au3C2
Date: 2021-01-07 09:29:36
LastEditors: Au3C2
LastEditTime: 2021-01-07 09:34:36
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circles += 1
        
        return circles
# 图，完全不会
# https://leetcode-cn.com/problems/number-of-provinces/