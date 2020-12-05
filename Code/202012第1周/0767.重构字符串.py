'''
Description: 
Autor: Au3C2
Date: 2020-11-30 10:22:27
LastEditors: Au3C2
LastEditTime: 2020-11-30 16:45:38
'''
class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2:
            return S
        
        length = len(S)
        counts = collections.Counter(S)
        maxCount = max(counts.items(), key=lambda x: x[1])[1]
        if maxCount > (length + 1) // 2:
            return ""
        
        queue = [(-x[1], x[0]) for x in counts.items()]
        heapq.heapify(queue)
        ans = list()

        while len(queue) > 1:
            n1, letter1 = heapq.heappop(queue)
            n2, letter2 = heapq.heappop(queue)
            # n = min(-n1,-n2)
            ans.extend([letter1, letter2]*-n2)
            if (-n1+n2) > 0:
                heapq.heappush(queue, (n1-n2, letter1))
       
        if queue:
            ans.append(queue[0][1])
        
        return "".join(ans)