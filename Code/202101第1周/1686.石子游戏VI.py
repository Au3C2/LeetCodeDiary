'''
Description: 
Autor: Au3C2
Date: 2021-01-07 16:05:51
LastEditors: Au3C2
LastEditTime: 2021-01-07 16:06:17
'''
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        import numpy as np
        n = len(aliceValues)
        aliceValues = np.array(aliceValues,dtype=np.uint8)
        bobValues = np.array(bobValues,dtype=np.uint8)
        sumValues = aliceValues + bobValues
        idx = (np.argsort(sumValues))[::-1]
        score = 0
        for i in range(n):
            if i%2 : # bob回合
                score -= bobValues[idx[i]]
            else : # alice回合
                score += aliceValues[idx[i]]
        if score > 0:
            return 1
        elif score < 0:
            return -1
        else:
            return 0
# 贪心，中等，稍显简单了
# https://leetcode-cn.com/problems/stone-game-vi/