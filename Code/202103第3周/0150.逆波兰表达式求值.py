'''
Description: 
Autor: Au3C2
Date: 2021-03-20 11:03:35
LastEditors: Au3C2
LastEditTime: 2021-03-20 11:03:55
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for c in tokens:
            if c == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif c == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif c == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif c == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))  
            else:
                stack.append(int(c))
                
        return stack[0]

# 栈，中等
# https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/