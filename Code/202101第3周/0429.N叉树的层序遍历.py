'''
Description: 
Autor: Au3C2
Date: 2021-01-20 12:31:06
LastEditors: Au3C2
LastEditTime: 2021-01-20 12:31:20
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = [[root.val]]
        lastLevel = [root]
        thisLevel = list() # 记录结点信息
        t = list() # 记录节点值
        flag = True if root.children else False # 记录是否有下一层的信息
        while flag:
            flag = False
            t = list() # 记录节点值
            thisLevel = list() # 记录结点信息
            for node in lastLevel:
                for c in node.children:
                    thisLevel.append(c)
                    t.append(c.val)
                    if c.children != None: # 存在下一层
                        flag = True
            if t:
                ans.append(t)
            lastLevel = thisLevel
        return ans

# 树，中等
# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/