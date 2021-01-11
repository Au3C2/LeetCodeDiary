'''
Description: 
Autor: Au3C2
Date: 2021-01-06 10:11:06
LastEditors: Au3C2
LastEditTime: 2021-01-06 10:11:43
'''
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        f = {}
        d = {}

        def find(x):
            f.setdefault(x, x)
            d.setdefault(x,1)
            if x != f[x]:
                t = f[x]
                f[x] = find(t)
                d[x] *= d[t]
                return f[x]
            return x 

        def union(A, B, value):
            a, b = find(A), find(B)
            if a != b:
                f[a] = b
                d[a] = d[B] / d[A] * value

        def check(x, y):
            if x not in f or y not in f:
                return -1.0
            a, b = find(x), find(y)
            if a != b:
                return -1.0
            return d[x] / d[y]

        for i, nums in enumerate(equations):
            union(nums[0], nums[1], values[i])
        res = []
        for x, y in queries:
            res.append(check(x, y))
        return res

# 并查集，图。中等，每日一题，完全不会呢
# https://leetcode-cn.com/problems/evaluate-division/