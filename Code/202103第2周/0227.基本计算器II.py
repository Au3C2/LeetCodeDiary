'''
Description: 
Autor: Au3C2
Date: 2021-03-11 12:22:07
LastEditors: Au3C2
LastEditTime: 2021-03-11 15:02:12
'''
class Solution:
    def calculate(self, s):
        s = s.replace(' ','')
        stack = list()
        lastOpra = False
        n = len(s)
        i = 0    
        while i < n :
            if s[i].isdigit():
                num2 = int(s[i])
                while i<n-1 and s[i+1].isdigit():
                    num2 = num2*10 + int(s[i+1])
                    i += 1
                i += 1
                if lastOpra =='*' or lastOpra == '/':
                    num1 = stack.pop()
                    t = num1 * num2 if lastOpra == '*' else int(num1 / num2)
                    stack.append(t)
                    lastOpra = False
                elif lastOpra=='-':
                    stack.append(-1*num2)
                else:
                    stack.append(num2)
            else:
                lastOpra = s[i]
                i += 1           
        return sum(stack)
# 栈，中等。不用eval()，速度快很多
# https://leetcode-cn.com/problems/basic-calculator-ii/