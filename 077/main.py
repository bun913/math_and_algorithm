"""
これも問題076と同じく足される数を考える
まずXとYは分けて考えて良い
かつ、X・Yそれぞれの点とのマンハッタン距離を測る
つまり配列をソートしても結果に変わりはなし
"""
N = int(input())
X = []
Y = []

for _ in range(N):
    x,y = list(map(int, input().split()))
    X.append(x)
    Y.append(y)

xd = sorted(X, reverse=True)
yd = sorted(Y, reverse=True)
ans = 0

for i in range(N):
    x = xd[i]
    y = yd[i]
    ans += (N-2*i-1) * x
    ans += (N-2*i-1) * y
print(ans)