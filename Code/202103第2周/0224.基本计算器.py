'''
Description: 
Autor: Au3C2
Date: 2021-03-10 14:37:36
LastEditors: Au3C2
LastEditTime: 2021-03-10 14:38:28
'''
class Solution(object):
    def calculate(self, s):
        stack = []
        for c in s:
            if c.isdigit() or c == '-' or c == '+' or c =='(':
                stack.append(c)
            elif c==')':
                t = list()
                while stack[-1] != '(':
                    t.append(stack.pop())
                stack.pop() # 弹出"("
                stack.append(str(eval(''.join(t[::-1]))))
                
        return eval(''.join(stack))

# 栈，困难，虽然只超过50%，但是是自己写的！
# https://leetcode-cn.com/problems/basic-calculator/