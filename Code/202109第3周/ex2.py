'''
Description: 百度笔试2
Autor: Au3C2
Date: 2021-09-14 20:12:54
LastEditors: Au3C2
LastEditTime: 2021-09-15 11:08:28
6
1 8 3 6 7 5
1 2 3 6 9 7

'''
n = int(input().strip())
A = [int(x) for x in input().strip().split(' ')]
B = [int(x) for x in input().strip().split(' ')]

n1, s1 = 0, 1
for i in range(1, len(A)):
    n2, s2 = float("inf"), float("inf")
    if A[i-1] < A[i]:
        n2 = min(n2, n1)
        s2 = min(s2, s1 + 1)
    if A[i-1] < B[i]:
        n2 = min(n2, s1)
        s2 = min(s2, n1 + 1)

    n1, s1 = n2, s2

print(min(n1, s1))