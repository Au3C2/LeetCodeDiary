<!--
 * @Description: 
 * @Autor: Au3C2
 * @Date: 2021-07-19 14:32:36
 * @LastEditors: Au3C2
 * @LastEditTime: 2021-07-19 14:32:43
-->
# [剑指 Offer 42. 连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

 

**示例1:**

```
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

 

**提示：**

-   `1 <= arr.length <= 10^5`
-   `-100 <= arr[i] <= 100`

动态规划 简单

做过的题

# 代码

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        ans = nums[0]
        for n in nums:
            pre = max(pre+n,n)
            ans = max(ans,pre)
        return ans
```

