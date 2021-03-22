'''
Description: 
Autor: Au3C2
Date: 2021-03-19 16:58:28
LastEditors: Au3C2
LastEditTime: 2021-03-19 16:58:55
'''
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.target = target.val
        self.res = None
        self.recursion(cloned)
        return self.res
    def recursion(self,root):
        if not root or self.res:
            return
        if root.val == self.target:
            self.res = root
        self.recursion(root.left)
        self.recursion(root.right)

# 树，中等。奇怪的题目
# https://leetcode-cn.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/