<!--
 * @Description: 
 * @Autor: Au3C2
 * @Date: 2021-07-16 10:25:47
 * @LastEditors: Au3C2
 * @LastEditTime: 2021-07-16 10:26:05
-->
# [剑指 Offer 53 - I. 在排序数组中查找数字 I](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)

统计一个数字在排序数组中出现的次数。

 

**示例 1:**

```
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
```

**示例 2:**

```
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
```

 

**限制：**

```
0 <= 数组长度 <= 50000
```

 

**注意：**本题与[主站 34 题](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)相同（仅返回值不同）：

二分查找 简单

二分查找后向两侧扩散即可

# 代码

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        lp, rp = idx-1, idx
        ans = 0
        while lp >= 0:
            if nums[lp] == target:
                ans += 1
            else:
                break
            lp -= 1
        while rp < len(nums):
            if nums[rp] == target:
                ans += 1
            else:
                break
            rp += 1
        return ans
```

