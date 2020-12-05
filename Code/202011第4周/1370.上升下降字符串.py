class Solution:
    def sortString(self, s: str) -> str:
        count = collections.Counter(s)
        n = len(s)
        output = []
        l_s = sorted(list(count.keys()))
        il_s = l_s[::-1]
        while n:
            for c in l_s:
                # c = chr(i)
                if count[c] > 0:
                    output.append(c)
                    count[c] -= 1
                    n -= 1
            for c in il_s:
                # c = chr(i)
                if count[c] > 0:
                    output.append(c)
                    count[c] -= 1
                    n -= 1
        return ''.join(output)