class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}
        for sc, tc in zip(s,t):
            if sc in s2t and s2t[sc] != tc:
                return False
            else:
                s2t[sc] = tc
            if tc in t2s and t2s[tc] != sc:
                return False          
            else:
                t2s[tc] = sc
        for sc,tc in s2t.items():
            if t2s[tc] != sc:
                return False
        for tc,sc in t2s.items():
            if s2t[sc] != tc:
                return False
        return True
# 哈希表，简单
# https://leetcode-cn.com/problems/isomorphic-strings/