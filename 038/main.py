"""
"""
from itertools import accumulate

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
acc = list(accumulate(A))
acc.insert(0,0)

for _ in range(Q):
    l,r = list(map(int, input().split()))
    ans = acc[r] - acc[l-1]
    print(ans)