```python
'''
Description: 
Autor: Au3C2
Date: 2021-01-16 15:40:31
LastEditors: Au3C2
LastEditTime: 2021-01-16 15:40:45
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def mirrorTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		# 递归函数的终止条件，节点为空时返回
		if not root:
			return None
		# 将当前节点的左右子树交换
		root.left,root.right = root.right,root.left
		# 递归交换当前节点的 左子树和右子树
		self.mirrorTree(root.left)
		self.mirrorTree(root.right)
		# 函数返回时就表示当前这个节点，以及它的左右子树
		# 都已经交换完了		
		return root

# 树，简单
# https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/
```
