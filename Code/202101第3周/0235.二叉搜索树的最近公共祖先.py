'''
Description: 
Autor: Au3C2
Date: 2021-01-21 16:09:22
LastEditors: Au3C2
LastEditTime: 2021-01-21 16:09:31
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root
        while True:
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor
# 树，简单
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/