'''
Description: 
Autor: Au3C2
Date: 2021-01-20 11:14:30
LastEditors: Au3C2
LastEditTime: 2021-01-20 11:15:04
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftLength = self.maxDepth(root.left)
        rightLength = self.maxDepth(root.right)
        return max(leftLength,rightLength) + 1
# 树，简单，与 剑指Offer55-I.二叉树的深度 相同，自己重写了一遍
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/