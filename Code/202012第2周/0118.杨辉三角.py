class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        output = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        for n in range(2,numRows): # 第n行,同时也是该行长度
            row = [1] # 这一行初始化
            for i in range(1,(n+1)//2+1): #因为是对称的仅需跑出一半的值
                row.append(output[n-1][i-1]+output[n-1][i])
            temp = row[:-1] if (n+1)%2==1 else row[:-2]
            row.extend(temp[::-1])
            output.append(row)
        return output
# 简单题，有大一c语言的感觉了。
# tag数组