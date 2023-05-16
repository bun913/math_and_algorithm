"""
素因数分解するプログラムを作る
Nが10**12なので普通に2から順番に割っていくと間に合わない
最大でもsqrt(N)まで調べればOK
"""
from math import sqrt

N = int(input())
now = N
ans = []

for i in range(2,int(sqrt(N)) + 1):
    while now % i == 0:
        now //= i
        ans.append(i)
if now != 1:
    ans.append(now)
print(*ans)