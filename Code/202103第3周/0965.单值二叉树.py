'''
Description: 
Autor: Au3C2
Date: 2021-03-18 16:28:34
LastEditors: Au3C2
LastEditTime: 2021-03-18 16:28:59
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.n = root.val
        return self.recursion(root)

    def recursion(self,root):
        
        if not root:
            return True
        
        left = self.recursion(root.left)
        right = self.recursion(root.right)
        
        if root.val == self.n and left and right:
            return True
        else:
            return False

# 树，简单
# https://leetcode-cn.com/problems/univalued-binary-tree/