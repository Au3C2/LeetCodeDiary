'''
Description: 
Autor: Au3C2
Date: 2021-01-19 16:12:00
LastEditors: Au3C2
LastEditTime: 2021-01-19 16:14:55
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        mid = len(nums) // 2
        if not nums:
            return
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:]) 
        return root
# 树，简单
# https://leetcode-cn.com/problems/minimum-height-tree-lcci/