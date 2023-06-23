"""
特定の区画にだけ雪が降る
最終的に積雪量を考えて、i番目の区画がi+1番目の区画と雪の量がどうか考える
ようは最終的に1個前の項との差、階差を求めれば良い
でLからRまで雪が降ると言うことは
L番目の区画の階差に+1して、R+1番目の区画の階差に-1する
"""
N, Q = list(map(int, input().split()))
# 階差を保持する配列
dif = [0] * (N)
for _ in range(Q):
    L, R, X = list(map(int, input().split()))
    dif[L-1] += X
    if R < N:
        dif[R] -= X
ans = []
for i in range(1,N):
    # i+1の方から見るので逆になる
    if dif[i] > 0:
        ans.append("<")
    elif dif[i] == 0:
        ans.append("=")
    else:
        ans.append(">")
print(*ans, sep='')