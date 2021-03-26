```python
'''
Description: 
Autor: Au3C2
Date: 2020-12-23 16:14:15
LastEditors: Au3C2
LastEditTime: 2020-12-23 16:15:02
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        ans = nums[0]
        for n in nums:
            pre = max(pre+n,n)
            ans = max(ans,pre)
        return ans
# 动态规划简单题。动态规划的题都不简单啊
# https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/

```
