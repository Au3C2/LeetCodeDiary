'''
Description: 
Autor: Au3C2
Date: 2021-03-18 16:09:30
LastEditors: Au3C2
LastEditTime: 2021-03-18 16:09:47
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head      
        node = TreeNode(0)
        node.next = head
        head = node

        ori_head = head
        # head = head.next
        
        last_node = head.next      # 指向 1 节点
        this_node = last_node.next # 指向 2 节点

        while this_node:
            last_node.next = this_node.next
            this_node.next = head.next
            head.next = this_node
            this_node = last_node.next
        return ori_head.next

# 链表，简单
# https://leetcode-cn.com/problems/reverse-linked-list/