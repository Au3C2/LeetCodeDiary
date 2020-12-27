'''
Description: 
Autor: Au3C2
Date: 2020-12-23 09:22:36
LastEditors: Au3C2
LastEditTime: 2020-12-23 09:23:28
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # 特殊情况处理
        if not root:
            return []        
        # queue 队列先存入根节点
        queue = deque()
        queue.append(root)
        
        # 用来标记当前层是偶数层还是奇数层
        is_even_level = True
        # 结果列表
        ans = []
        
        # 队列不为空时，开始进行遍历
        while queue:
            # 声明双端队列 level_queue
            level_queue = deque()
            # 先计算 queue 的长度 size
            size = len(queue)
            
            # 取出 size 个元素
            for _ in range(size):
                # 取出节点
                node = queue.popleft()
                # 偶数层，将节点值插入到 level_queue 尾部
                if is_even_level:
                    level_queue.append(node.val)
                # 奇数层，将节点值插入到 level_queue 头部
                else:
                    level_queue.appendleft(node.val)
                # 将下一层的节点存放到 queue 中
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 这里注意，将双端队列转换为列表的形式，存入结果列表中
            ans.append(list(level_queue))
            # 维护更新 is_even_level
            is_even_level = not is_even_level
        
        return ans

# 二叉树，中等，不会做呢
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/solution/er-cha-shu-de-ju-chi-xing-ceng-xu-bian-l-qsun/