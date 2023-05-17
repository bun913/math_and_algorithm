"""
これも組み合わせの問題
3色のカードがあって、そこから同じ色のカードを2枚選ぶ方法を求める
Nで求められる
"""
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
C = Counter(A)

ans = 0
for c in C.most_common():
    cnt = c[1]
    if cnt <= 1:
        continue
    ans += cnt * (cnt-1) // 2
print(ans)