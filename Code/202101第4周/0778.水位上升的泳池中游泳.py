'''
Description: 
Autor: Au3C2
Date: 2021-01-30 10:07:37
LastEditors: Au3C2
LastEditTime: 2021-01-30 10:08:19
'''
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        heap = [(grid[0][0],0,0)]
        visited = set([(0,0)])
        
        while heap:
            height,x,y = heapq.heappop(heap)
            res = max(res,height)
            if x == n-1 and y == n-1:
                return res
            
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_x,new_y = x + dx,y + dy
                if 0 <= new_x < n and 0 <= new_y < n and (new_x,new_y) not in visited:
                    visited.add((new_x,new_y))
                    heapq.heappush(heap,(grid[new_x][new_y],new_x,new_y))
        
        return -1
# 并查集\困难\每日一题 看到并查集直接不想做了
# https://leetcode-cn.com/problems/swim-in-rising-water/