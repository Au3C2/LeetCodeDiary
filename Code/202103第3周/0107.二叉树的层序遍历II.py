'''
Description: 
Autor: Au3C2
Date: 2021-03-19 10:49:49
LastEditors: Au3C2
LastEditTime: 2021-03-19 10:56:59
'''
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = list()
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if level:
                res.append(level)
        return res[::-1]

# 树，中等
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/