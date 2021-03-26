```python
'''
Description: 
Autor: Au3C2
Date: 2021-01-20 16:58:50
LastEditors: Au3C2
LastEditTime: 2021-01-20 17:06:40
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def recursion(root,k):
            if not root or self.idx >= k:
                return
            recursion(root.right,k)
            self.idx += 1
            if self.idx == k:
                self.ans = root.val
                return
            recursion(root.left,k)
        self.idx = 0
        self.ans = None
        recursion(root,k)
        return self.ans
# 树，简单，二分查找
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/
```
