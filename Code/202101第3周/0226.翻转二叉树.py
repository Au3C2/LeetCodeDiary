'''
Description: 
Autor: Au3C2
Date: 2021-01-20 10:23:57
LastEditors: Au3C2
LastEditTime: 2021-01-20 10:25:02
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return

        t = root.left
        root.left = root.right
        root.right = t

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root
# 树，简单，和 剑指Offer27.二叉树的镜像 是同一题，自己又重写了一遍
# https://leetcode-cn.com/problems/invert-binary-tree/