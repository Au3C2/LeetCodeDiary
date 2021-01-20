'''
Description: 
Autor: Au3C2
Date: 2021-01-20 11:25:27
LastEditors: Au3C2
LastEditTime: 2021-01-20 11:25:44
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def recursion(root):
            if not root:
                return
            for c in root.children:
                recursion(c)
            self.ans.append(root.val)

        self.ans = []
        recursion(root)
        return self.ans
# 树，简单
# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/