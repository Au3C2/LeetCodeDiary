'''
Description: 
Autor: Au3C2
Date: 2021-03-11 12:22:07
LastEditors: Au3C2
LastEditTime: 2021-03-11 12:22:40
'''
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        stack = []
        lastFlag = False
        n = len(s)
        i = 0    
        while i < n :

            if s[i].isdigit():
                t = list(s[i])
                while i<n-1 and s[i+1].isdigit():
                    t.append(s[i+1])
                    i += 1
                i += 1
                stack.append(''.join(t))
                
                if lastFlag:
                    num2, operator, num1 = int(stack.pop()), stack.pop(), int(stack.pop())
                    t = num1 * num2 if operator == '*' else math.floor(num1 / num2)
                    stack.append(str(t))
                    lastFlag = False

            else:
                stack.append(s[i])
                if s[i]=='*' or s[i] == '/':
                    lastFlag = s[i]
                i += 1
            
            # if s[i]=='*' or s[i] == '/':
            #     lastFlag = s[i]
                
        return eval(''.join(stack))

# 栈，中等
# https://leetcode-cn.com/problems/basic-calculator-ii/