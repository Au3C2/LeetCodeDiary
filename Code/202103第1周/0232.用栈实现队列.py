'''
Description: 
Autor: Au3C2
Date: 2021-03-05 10:49:19
LastEditors: Au3C2
LastEditTime: 2021-03-05 10:50:17
'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = list()


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if self.stack else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# 栈，简单。懒得写，作弊用列表实现了
# https://leetcode-cn.com/problems/implement-queue-using-stacks/