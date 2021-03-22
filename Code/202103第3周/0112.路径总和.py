'''
Description: 
Autor: Au3C2
Date: 2021-03-15 18:58:46
LastEditors: Au3C2
LastEditTime: 2021-03-15 18:59:17
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.targetSum = targetSum
        return True if self.path_sum(root,0) else False
    def path_sum(self, root, sum_r):
        if not root:
            return
        else:
            sum_r += root.val
        
        if not root.left and not root.right:
            return sum_r == self.targetSum
        
        return True if (self.path_sum(root.left, sum_r) or self.path_sum(root.right, sum_r)) else False

# 树，简单
# https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers/