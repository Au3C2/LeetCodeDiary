<!--
 * @Description: 
 * @Autor: Au3C2
 * @Date: 2021-06-22 12:09:55
 * @LastEditors: Au3C2
 * @LastEditTime: 2021-06-22 15:49:19
-->
# [剑指 Offer 38. 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)



输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

**示例:**

```
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
```

 

**限制：**

```
1 <= s 的长度 <= 8
```
回溯 中等

需要剪枝
# [思路](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/mian-shi-ti-38-zi-fu-chuan-de-pai-lie-hui-su-fa-by/)

# 代码

## 1. 我的代码，没有剪枝过程
```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s: 
            return ''
        ans = []
        for i,c in enumerate(s):
            res = self.permutation(s[:i]+s[i+1:])
            for r in res:
                ans.append(c+r)
            if res == '':
                ans.append(c)
        return list(set(ans))
```

## 2. 某个[题解](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/mian-shi-ti-38-zi-fu-chuan-de-pai-lie-hui-su-fa-by/)的代码
```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))   # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)               # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换
        dfs(0)
        return res
```