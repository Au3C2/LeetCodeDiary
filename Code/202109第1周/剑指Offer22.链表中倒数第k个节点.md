<!--
 * @Description: 
 * @Autor: Au3C2
 * @Date: 2021-09-02 11:06:19
 * @LastEditors: Au3C2
 * @LastEditTime: 2021-09-02 11:06:19
-->
# [剑指 Offer 22. 链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/)

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 `6` 个节点，从头节点开始，它们的值依次是 `1、2、3、4、5、6`。这个链表的倒数第 `3` 个节点是值为 `4` 的节点。

 

**示例：**

```
给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.
```

链表 双指针 简单

# 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        lp, rp = dummy, dummy
        diff = 0
        while rp and diff < k:
            rp = rp.next
            diff += 1
        while rp:
            rp = rp.next
            lp = lp.next
        return lp
```

