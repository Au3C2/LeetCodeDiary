```python
'''
Description: 
Autor: Au3C2
Date: 2020-12-14 15:21:56
LastEditors: Au3C2
LastEditTime: 2020-12-14 15:23:56
'''
import queue
class MaxQueue:

    def __init__(self):
        self.deque = queue.deque()
        self.queue = queue.Queue()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1


    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

# 堆题，不知道为啥放到滑窗来了，直接借用python库实现了，不重复造轮子（也造不来
# https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/
```
