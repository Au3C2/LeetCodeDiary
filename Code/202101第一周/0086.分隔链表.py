'''
Description: 
Autor: Au3C2
Date: 2021-01-04 10:55:56
LastEditors: Au3C2
LastEditTime: 2021-01-04 10:59:06
'''
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p=less=ListNode(0)
        q=more=ListNode(0)

        while head:
            if head.val<x:
                less.next=head
                less=less.next
            else:
                more.next=head
                more=more.next
            head=head.next

        more.next=None
        less.next=q.next
        return p.next
# 链表，中等，每日一题，并不会
# https://leetcode-cn.com/problems/partition-list/