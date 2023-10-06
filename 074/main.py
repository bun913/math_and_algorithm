"""
足される回数と引かれる回数を考える問題
これは考え方を知ってないと絶対に解けない気がする
逆に考え方を知っていれば、実装自体は楽
"""
from functools import reduce

N = int(input())
A = list(map(int, input().split()))
ans = 0
for i, a in enumerate(A):
    ans += a * (2 * i - N + 1)
print(ans)