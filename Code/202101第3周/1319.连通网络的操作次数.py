'''
Description: 
Autor: Au3C2
Date: 2021-01-25 16:32:49
LastEditors: Au3C2
LastEditTime: 2021-01-25 16:33:20
'''
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        edges = collections.defaultdict(list)
        for x, y in connections:
            edges[x].append(y)
            edges[y].append(x)
        
        seen = set()

        def dfs(u: int):
            seen.add(u)
            for v in edges[u]:
                if v not in seen:
                    dfs(v)
        
        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        
        return ans - 1

# 并查集，中等，每日一题。不会做
# https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected/