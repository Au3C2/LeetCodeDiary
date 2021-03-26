```python
'''
Description: 
Autor: Au3C2
Date: 2021-01-21 16:05:38
LastEditors: Au3C2
LastEditTime: 2021-01-21 16:07:54
'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recursion(root,p,q):
            if not root or root == p or root == q: return root
            left = recursion(root.left, p, q)
            if self.flag: # 提早结束递归，比原版能快个20ms
                return left
            right = recursion(root.right, p, q)
            if self.flag: # 提早结束递归，比原版能快个20ms
                return right 
            if not left: return right
            if not right: return left
            self.flag = True
            return root
        self.flag = False
        return recursion(root,p,q)
# 树，简单
# https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recursion(root,t):
            if not root:
                return False
            path.append(root.val)
            if root.val == t:
                return True
            leftFlag = recursion(root.left,t)
            rightFlag = recursion(root.right,t)
            if leftFlag or rightFlag:
                return True
            elif not leftFlag and not rightFlag:
                path.pop()
        path = list()
        recursion(root,p.val)
        path_p = list(path)
        path = list()
        recursion(root,q.val)
        for i,j in zip(path_p,path):
            if i == j:
                ans = i
        return TreeNode(ans)

# 这是我的解法，记录两条路径。这是比较直接的思路了

```
