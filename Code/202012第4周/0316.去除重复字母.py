class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for idx, char in enumerate(s):
            if char in stack:continue
            while stack and char < stack[-1] and stack[-1] in s[idx:]:
                stack.pop()
            stack.append(char)
        return "".join(stack)

# 每日一题，栈，贪心
# https://leetcode-cn.com/problems/remove-duplicate-letters/