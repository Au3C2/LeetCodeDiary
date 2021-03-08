'''
Description: 
Autor: Au3C2
Date: 2021-03-07 10:49:04
LastEditors: Au3C2
LastEditTime: 2021-03-07 10:49:33
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return
            
            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret
    
# dfs,动态规划，中等。也是不想做题的一天

# https://leetcode-cn.com/problems/palindrome-partitioning/ 