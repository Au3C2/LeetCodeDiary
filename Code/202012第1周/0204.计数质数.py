'''
Description: 
Autor: Au3C2
Date: 2020-12-03 10:56:18
LastEditors: Au3C2
LastEditTime: 2020-12-03 10:58:30
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        import numpy as np
        if n < 2:
            return 0

        isPrime = np.ones(n, dtype=np.bool_)
        isPrime[0] = isPrime[1] = 0

        for i in np.arange(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = 0

        return int(np.sum(isPrime))

# 用上了埃拉托斯特尼筛法，简单地说就是排除范围内的和数，剩下的都是质数。
# https://leetcode-cn.com/problems/count-primes/solution/pythonzui-you-jie-fa-mei-you-zhi-yi-liao-ba-by-bru/
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
