'''
Description: 
Autor: Au3C2
Date: 2021-03-12 10:55:06
LastEditors: Au3C2
LastEditTime: 2021-03-12 10:55:33
'''
class Solution(object):
    def isValidSerialization(self, preorder):
        nodes = preorder.split(',')
        diff = 1
        for node in nodes:
            diff -= 1
            if diff < 0:
                return False
            if node != '#':
                diff += 2
        return diff == 0
# 栈，中等，计算出入度即可
# https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/