'''
Description: 
Autor: Au3C2
Date: 2021-02-18 12:11:26
LastEditors: Au3C2
LastEditTime: 2021-02-18 12:12:31
'''
class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        que = collections.deque()
        res = 0
        for i in range(N):
            if que and i >= que[0] + K:
                que.popleft()
            if len(que) % 2 == A[i]:
                if i +  K > N: return -1
                que.append(i)
                res += 1
        return res

# 数组，困难，每日一题，开工啦
# https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips/
# 比较难理解，看这个题解：https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips/solution/hua-dong-chuang-kou-shi-ben-ti-zui-rong-z403l/