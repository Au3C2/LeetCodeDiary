'''
Description: 
Autor: Au3C2
Date: 2021-01-20 16:11:44
LastEditors: Au3C2
LastEditTime: 2021-01-20 16:16:18
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        mid = len(nums) // 2
        if not nums:
            return
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:]) 
        return root
# 树，简单，和 面试题04.02.最小高度树 相同
# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/