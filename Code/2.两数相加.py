#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建一个结点值为 None 的头结点, dummy 和 p 指向头结点, dummy 用来最后返回, p 用来遍历
        # dummy = p = ListNode(None)          
        # s = 0               # 初始化进位 s 为 0
        # while l1 or l2 or s:
        #     # 如果 l1 或 l2 存在, 则取l1的值 + l2的值 + s(s初始为0, 如果下面有进位1, 下次加上)
        #     s += (l1.val if l1 else 0) + (l2.val if l2 else 0)  
        #     p.next = ListNode(s % 10)       # p.next 指向新链表, 用来创建一个新的链表
        #     p = p.next                      # p 向后遍历
        #     s //= 10                        # 有进位情况则取模, eg. s = 18, 18 // 10 = 1
        #     l1 = l1.next if l1 else None    # 如果l1存在, 则向后遍历, 否则为 None
        #     l2 = l2.next if l2 else None    # 如果l2存在, 则向后遍历, 否则为 None
        # return dummy.next   # 返回 dummy 的下一个节点, 因为 dummy 指向的是空的头结点, 下一个节点才是新建链表的后序节点
        # 创建一个结点值为 None 的头结点, dummy 和 p 指向头结点, dummy 用来最后返回, p 用来遍历
        # head = p = ListNode(None)          
        s = 0               # 初始化进位 s 为 0
        head = l1
        while l1 or l2 or s:
            # 如果 l1 或 l2 存在, 则取l1的值 + l2的值 + s(s初始为0, 如果下面有进位1, 下次加上)
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)  
            
            if l1:     
                l1.val = s % 10    # 假如l1有这一节点，直接覆盖
            else:
                last_l1.next = ListNode(s%10,None) # 假如l1没有这一节点，新建一个
                l1 = last_l1.next
            s //= 10                        
            last_l1 = l1
            l1 = l1.next if l1 else None    
            l2 = l2.next if l2 else None   
        return head   # 返回 dummy 的下一个节点, 因为 dummy 指向的是空的头结点, 下一个节点才是新建链表的后序节点

# @lc code=end

