'''
Description: 
Autor: Au3C2
Date: 2021-01-21 16:02:13
LastEditors: Au3C2
LastEditTime: 2021-01-21 16:02:38
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = [[root.val]]
        lastLevel = [root]
        thisLevel = list() # 记录结点信息
        t = list() # 记录节点值
        flag = True if (root.left or root.right) else False # 记录是否有下一层的信息
        while flag:
            flag = False
            t = list() # 记录节点值
            thisLevel = list() # 记录结点信息
            for node in lastLevel:
                for c in [node.left,node.right]:
                    if c:
                        thisLevel.append(c)
                        t.append(c.val)
                        if c.left or c.right: # 存在下一层
                            flag = True
            if t:
                ans.append(t)
            lastLevel = thisLevel
        return ans

# 树，简单。二叉树的层序遍历
# https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/