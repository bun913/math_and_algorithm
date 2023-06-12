"""
一見何のこっちゃわからんけど、階差の問題だ
答えが[0,1,...,T-1]に何人の従業員がいるか答える問題
なので階差で答えを保持しておけば良いだけだわ
"""
from itertools import accumulate

T = int(input())
N = int(input())
dif = [0 for _ in range(T+1)]
for _ in range(N):
    l, r = map(int, input().split())
    dif[l] += 1
    dif[r] -= 1
# 階差の累積和が答え
ans = list(accumulate(dif))
for a in range(T):
    print(ans[a])