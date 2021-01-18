'''
Description: 
Autor: Au3C2
Date: 2021-01-15 15:06:27
LastEditors: Au3C2
LastEditTime: 2021-01-15 15:07:01
'''
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dict_X = collections.defaultdict(list)
        dict_Y = collections.defaultdict(list)
        for x, y in stones:
            dict_X[x].append((x, y))
            dict_Y[y].append((x, y))
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            x, y = node
            for i in dict_X[x]:
                dfs(i)
            for i in dict_Y[y]:
                dfs(i)
        
        ans = 0
        for i in stones:
            i = tuple(i)
            if i not in visited:
                ans += 1
                dfs(i)
        
        return len(stones) - ans

# 深度优先搜索，中等，每日一题，暂时还不会
# https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/