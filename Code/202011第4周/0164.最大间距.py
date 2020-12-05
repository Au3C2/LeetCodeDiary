class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        l =  len(nums)
        if l < 2:
            return 0
        nums = sorted(nums)
        max_n =  float(-inf)
        for i in range(l-1):
            diff = abs(nums[i]-nums[i+1])
            if diff > max_n:
                max_n = diff
        return max_n