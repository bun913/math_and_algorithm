"""
これも典型的な累積和の問題
"""
from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
A.insert(0,0)
acc = list(accumulate(A))
M = int(input())
B = [int(input()) for _ in range(M)]

# B[i]をl,B[i+1]をrとして累積和から距離の合計を求める
# 面倒なのでl = min(l,r)としておく
ans = 0
for i in range(M-1):
    l = min(B[i], B[i+1])
    r = max(B[i], B[i+1])
    ans += acc[r-1] - acc[l-1]
print(ans)