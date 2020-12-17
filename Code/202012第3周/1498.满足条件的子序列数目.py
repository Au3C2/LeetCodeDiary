'''
Description: 
Autor: Au3C2
Date: 2020-12-16 17:27:35
LastEditors: Au3C2
LastEditTime: 2020-12-16 17:28:29
'''
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        P = 10**9 + 7
        f = [1] + [0] * (n - 1)
        for i in range(1, n):
            f[i] = f[i - 1] * 2 % P

        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            if nums[i] * 2 > target:
                break
            maxValue = target - nums[i]
            pos = bisect.bisect_right(nums, maxValue) - 1
            contribute = f[pos - i] if pos >= i else 0
            ans += contribute
        
        return ans % P

# 这个解法很不sliding window
# 推理详见https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/solution/man-zu-tiao-jian-de-zi-xu-lie-shu-mu-by-leetcode-s/
# 不再赘述