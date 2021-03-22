'''
Description: 
Autor: Au3C2
Date: 2021-03-15 18:58:13
LastEditors: Au3C2
LastEditTime: 2021-03-15 18:58:28
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        # 逐层遍历，反向递归
        return self.bin_sum(root, 0)

    
    def bin_sum(self, root, sum_r):
        if not root:
            return 0
        else:
            sum_r = sum_r * 2 + root.val
        
        if not root.left and not root.right:
            return sum_r
        
        return self.bin_sum(root.left, sum_r) + self.bin_sum(root.right, sum_r)

# 树，简单
# https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers/