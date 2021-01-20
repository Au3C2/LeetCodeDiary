'''
Description: 
Autor: Au3C2
Date: 2021-01-20 11:04:36
LastEditors: Au3C2
LastEditTime: 2021-01-20 11:05:02
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        if low < root.val < high:
            leftSum = self.rangeSumBST(root.left,low,high)
            rightSum = self.rangeSumBST(root.right,low,high)
            return root.val + leftSum + rightSum
        elif root.val <= low:
            rightSum = self.rangeSumBST(root.right,low,high)
            if root.val == low:
                return rightSum + root.val  
            else:
                return rightSum
        elif root.val >= high:
            leftSum = self.rangeSumBST(root.left,low,high)
            if root.val == high:
                return leftSum + root.val  
            else:
                return leftSum

# 树，简单，和题目想法差不多
# https://leetcode-cn.com/problems/range-sum-of-bst/