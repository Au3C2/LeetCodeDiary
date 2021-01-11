'''
Description: 
Autor: Au3C2
Date: 2021-01-07 10:52:45
LastEditors: Au3C2
LastEditTime: 2021-01-07 10:54:27
'''
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        f = [[0] * n for _ in range(n)]
        maxl = [[0] * n for _ in range(n)]
        maxr = [[0] * n for _ in range(n)]

        for left in range(n - 1, -1, -1):
            maxl[left][left] = maxr[left][left] = stoneValue[left]
            total = stoneValue[left]
            suml = 0
            i = left - 1
            for right in range(left + 1, n):
                total += stoneValue[right]
                while i + 1 < right and (suml + stoneValue[i + 1]) * 2 <= total:
                    suml += stoneValue[i + 1]
                    i += 1
                if left <= i:
                    f[left][right] = max(f[left][right], maxl[left][i])
                if i + 1 < right:
                    f[left][right] = max(f[left][right], maxr[i + 2][right])
                if suml * 2 == total:
                    f[left][right] = max(f[left][right], maxr[i + 1][right])
                maxl[left][right] = max(maxl[left][right - 1], total + f[left][right])
                maxr[left][right] = max(maxr[left + 1][right], total + f[left][right])
        
        return f[0][n - 1]
# 优化后的动态规划，困难
# https://leetcode-cn.com/problems/stone-game-v/

# 我的解法没问题，就是超出时间限制了
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        sumWindow = [0]
        # sumWindow[0] = stoneValue[0]
        for i in range(n):
            sumWindow.append(sumWindow[-1]+stoneValue[i])
            
        dp = [[0] * n for _ in range(n)]
        for w in range(1,n):
            i = 0 # 开始下标
            j = i + w # 结束下标
            while j < n:
                t = []
                # sumW = sum()
                for p in range(i+1,j+1):
                    leftSum = sumWindow[p] - sumWindow[i]
                    rightSum = sumWindow[j+1] - sumWindow[p]
                    
                    if leftSum > rightSum:
                        t.append(rightSum+dp[p][j])
                    elif leftSum < rightSum:
                        t.append(leftSum+dp[i][p-1])
                    else:
                        t.append(rightSum+max(dp[p][j],dp[i][p-1]))
                
                dp[i][j] = max(t)
                i += 1
                j = i + w
        return dp[0][-1]   