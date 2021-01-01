'''
Description: 
Autor: Au3C2
Date: 2020-12-28 16:21:59
LastEditors: Au3C2
LastEditTime: 2020-12-28 16:24:57
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        dp = [0] * length
        for i, pile in enumerate(piles):
            dp[i] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[length - 1] > 0
        
# 动态规划，中等
# https://leetcode-cn.com/problems/stone-game/
# 讲解：https://leetcode-cn.com/problems/stone-game/solution/shi-zi-you-xi-qi-pi-lang-xi-lie-zhi-yi-r-ayk7/
# 因为先手必胜，也可以直接return True
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True