'''
Description: 
Autor: Au3C2
Date: 2021-03-15 16:47:04
LastEditors: Au3C2
LastEditTime: 2021-03-15 16:47:14
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if root.children:
            cLength = list()
            for c in root.children:
                cLength.append(self.maxDepth(c))
            return max(cLength) + 1
        else:
            return 1

# 树，简单
# https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/