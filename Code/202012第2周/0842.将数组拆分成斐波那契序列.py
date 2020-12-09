'''
Description: 
Autor: Au3C2
Date: 2020-12-09 09:16:53
LastEditors: Au3C2
LastEditTime: 2020-12-09 09:17:56
'''
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans = list()

        def backtrack(index: int):
            if index == len(S):
                return len(ans) >= 3
            
            curr = 0
            for i in range(index, len(S)):
                if i > index and S[index] == "0":
                    break
                curr = curr * 10 + ord(S[i]) - ord("0")
                if curr > 2**31 - 1:
                    break
                
                if len(ans) < 2 or curr == ans[-2] + ans[-1]:
                    ans.append(curr)
                    if backtrack(i + 1):
                        return True
                    ans.pop()
                elif len(ans) > 2 and curr > ans[-2] + ans[-1]:
                    break
        
            return False
        
        backtrack(0)
        return ans

# 没想多久就放弃了，又是贪心、回溯，都是没做过的题
# https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence/solution/jiang-shu-zu-chai-fen-cheng-fei-bo-na-qi-ts6c/