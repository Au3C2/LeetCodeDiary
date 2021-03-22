'''
Description: 
Autor: Au3C2
Date: 2021-03-16 17:04:58
LastEditors: Au3C2
LastEditTime: 2021-03-16 17:05:30
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        #对树做前序遍历同时做前缀和，同时记录祖先中的前缀和，在回溯时删除
        prefix_sum = collections.defaultdict(int) #记录路径中不同前缀和的数量
        prefix_sum[0] = 1 #哨兵，没有节点时和为0
        pre = 0 #从根节点到当前节点位置该路径的前缀和
        ans = 0
        def preOrder(root):
            nonlocal pre,prefix_sum,sum,ans
            if not root:
                return
            pre += root.val
            ans += prefix_sum[pre-sum]
            prefix_sum[pre] += 1

            preOrder(root.left)
            preOrder(root.right)

            prefix_sum[pre] -= 1
            pre -= root.val
        
        preOrder(root)
        return ans
        

# 树，中等，思路稍有不同，用上了前缀和，值得一看
# https://leetcode-cn.com/problems/path-sum-iii/