'''
Description: 
Autor: Au3C2
Date: 2021-03-13 09:48:15
LastEditors: Au3C2
LastEditTime: 2021-03-13 09:48:46
'''
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()


    def add(self, key: int) -> None:
        self.s.add(key)

    def remove(self, key: int) -> None:
        self.s.discard(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.s


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# 哈希表？，简单
# https://leetcode-cn.com/problems/design-hashset/