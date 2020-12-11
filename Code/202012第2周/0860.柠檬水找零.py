'''
Description: 
Autor: Au3C2
Date: 2020-12-10 09:19:07
LastEditors: Au3C2
LastEditTime: 2020-12-10 09:19:39
'''
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change5, change10 = 0,0
        for num in bills:
            if num ==5:
                change5 += 1
            if num == 10:
                if change5 > 0:
                    change5 -= 1
                    change10 += 1
                else:
                    return False
            if num == 20:
                if (change5>0 and change10>0):
                    change10 -= 1
                    change5 -= 1
                elif change5>=3:
                    change5 -=3
                else:
                    return False
        return True
# 简单题，枚举所有情况即可