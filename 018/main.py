"""
Nが200,000もある
2つを選ぶと10**10となり間に合わない
Nの時間計算量で求める必要がある
"""
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
C = Counter(A)

ans = 0
for combi in [(100,400), (200,300)]:
    l, r = combi
    ans += C[l] * C[r]
print(ans)