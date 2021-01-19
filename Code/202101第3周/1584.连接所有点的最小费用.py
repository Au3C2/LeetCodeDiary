'''
Description: 
Autor: Au3C2
Date: 2021-01-19 15:16:26
LastEditors: Au3C2
LastEditTime: 2021-01-19 15:40:18
'''
'''
rank数组是一种优化的方法，当并查集两个集合需要合并的时候，
把体量小的集合合并到体量大的下面，能够节省整个并查集的平均查找长度。
比如说，要把一个2个元素的集合和一个8个元素的集合合并，
那么选择将8个元素集合的parent作为2个元素集合parent的parent，
那么在后续查找的时候，那2个元素需要多往上查一步，但是那8个元素并不需要多查。
如果反过来的话，就是8个元素都需要多查一步，平均查找的效率就会低。
'''
class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))
    
    def find(self, x: int) -> int:
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]
    
    def unionSet(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])

        n = len(points)
        dsu = DisjointSetUnion(n)
        edges = list()

        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(i, j), i, j))
        
        edges.sort()
        
        ret, num = 0, 1
        for length, x, y in edges:
            if dsu.unionSet(x, y):
                ret += length
                num += 1
                if num == n:
                    break
        
        return ret
        
# 并查集，中等，每日一题。
# 仔细看了看，知识点缺漏还是比较多
# https://leetcode-cn.com/problems/min-cost-to-connect-all-points/