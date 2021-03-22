'''
Description: 
Autor: Au3C2
Date: 2021-03-17 16:53:59
LastEditors: Au3C2
LastEditTime: 2021-03-17 16:56:54
'''
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path = root.val
        self.recursion(root)
        return self.max_path
    def recursion(self,root):
        if not root:
            return 0
        left = max(self.recursion(root.left),0)
        right = max(self.recursion(root.right),0)
        inner_max = root.val + left + right
        self.max_path = max(inner_max,self.max_path)
        gain = root.val + max(left,right)
        return gain

# 树，困难，路径和终极版，值得复习
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/