'''
Description: 
Autor: Au3C2
Date: 2021-03-18 16:46:21
LastEditors: Au3C2
LastEditTime: 2021-03-19 10:46:44
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.level_dict = dict()
        self.recursion(root,0)
        res = list()
        for level in (self.level_dict).values():
            res.append(sum(level)/len(level))
        return res

    def recursion(self,root,level):
        
        if not root:
            return
        if level in self.level_dict:
            self.level_dict[level].append(root.val)
        else:
            self.level_dict[level] = list([root.val])
        level += 1
        self.recursion(root.left,level)
        self.recursion(root.right,level)
        level -= 1

# 树，简单
# https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = 0
            for _ in range(size):
                cur = queue.popleft()
                level += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if level != None:
                res.append(level/size)
        return res

# BFS解法