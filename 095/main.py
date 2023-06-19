"""
なんてわかりやすい累積和の問題なんだ
"""
from itertools import accumulate

N = int(input())
C1 = [0]
C2 = [0]
for _ in range(N):
    c, p = map(int, input().split())
    if c == 1:
        C1.append(p)
        C2.append(0)
    else:
        C1.append(0)
        C2.append(p)
cum1 = list(accumulate(C1))
cum2 = list(accumulate(C2))
Q = int(input())
for _ in range(Q):
    l , r = map(int, input().split())
    ans1 = cum1[r] - cum1[l-1]
    ans2 = cum2[r] - cum2[l-1]
    print(ans1, ans2, sep=" ")