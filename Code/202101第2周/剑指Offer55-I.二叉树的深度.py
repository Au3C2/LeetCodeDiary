'''
Description: 
Autor: Au3C2
Date: 2021-01-16 15:39:43
LastEditors: Au3C2
LastEditTime: 2021-01-16 15:40:00
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 0 if root is None else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# 树，简单
# https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/