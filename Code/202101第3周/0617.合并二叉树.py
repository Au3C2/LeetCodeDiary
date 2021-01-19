'''
Description: 
Autor: Au3C2
Date: 2021-01-19 16:45:55
LastEditors: Au3C2
LastEditTime: 2021-01-19 16:58:03
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left,t2.left)
            t1.right = self.mergeTrees(t1.right,t2.right)
        elif t1:
            pass
        elif t2:
            return t2
        else:
            return None
        
        return t1
# 树，简单题。
# https://leetcode-cn.com/problems/merge-two-binary-trees/