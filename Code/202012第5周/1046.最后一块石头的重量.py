'''
Description: 
Autor: Au3C2
Date: 2020-12-30 08:59:33
LastEditors: Au3C2
LastEditTime: 2020-12-30 08:59:52
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -i for i in stones]
        n = len(stones)
        heapq.heapify(stones)
        while n > 1:
            num = abs(heapq.heappop(stones) - heapq.heappop(stones))
            if num:
                heapq.heappush(stones, -num)
                n -= 1
            else:
                n -= 2
        return -stones[0] if n > 0 else 0
# 堆，简单，每日一题
# https://leetcode-cn.com/problems/last-stone-weight/