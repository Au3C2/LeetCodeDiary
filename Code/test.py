'''
Description: 
Autor: Au3C2
Date: 2020-11-24 12:46:57
LastEditors: Au3C2
LastEditTime: 2020-11-27 17:22:23
'''
import collections    
from collections import deque
    
def characterReplacement(s: str, k: int) -> int:
    n = len(s)
    if k >= n :
        return k
    if n == 0:
        return 0
    
    count = collections.Counter()
    lp = 0 #左指针
    # lookup = []
    max_len = k + 1
    cur_len = 0
    for rp in range(n): #右指针
        cur_len += 1
        count[s[rp]] += 1
        lookup = s[lp:rp+1]
        max_n = max(list(count.values()))
        if max_n == n:
            return n
        # if cur_len > isSatisfied(max_n,k,cur_len,max_len):
        if cur_len > max_len and max_n + k >= cur_len:
            max_len = cur_len
            
        if max_n + k < cur_len:
            count[s[lp]] -= 1
            lp += 1
            cur_len -= 1

    return max_len
    
something = characterReplacement("AAAA",2)
print(something)