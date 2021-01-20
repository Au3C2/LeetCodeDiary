'''
Description: 
Autor: Au3C2
Date: 2021-01-20 11:30:11
LastEditors: Au3C2
LastEditTime: 2021-01-20 11:31:40
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def recursion(root):
            if not root:
                return
            recursion(root.left)
            recursion(root.right)
            self.ans.append(root.val)
        self.ans = []
        recursion(root)
        return self.ans
        
# 树，中等。可以用迭代，但没必要
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/