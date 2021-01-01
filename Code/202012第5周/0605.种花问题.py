class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return False
            else:
                return True
        
        if flowerbed[0]+flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        if flowerbed[-1]+flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
            
        for i in range(1,len(flowerbed)-2):
            if flowerbed[i-1]+flowerbed[i]+flowerbed[i+1]==0:
                flowerbed[i] = 1
                n -= 1

        return n <= 0
# 贪心，简单，每日一题。直接遍历解决
# https://leetcode-cn.com/problems/can-place-flowers/