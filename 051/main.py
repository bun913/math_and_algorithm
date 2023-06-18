"""
数学的にいうと
(X + Y )! // X! * Y!が答えとなるはず
ただ、普通に計算するととんでもなく大きい数となってしまう
掛け算の場合は途中であまりをとっても良い性質であることを利用して考える
"""
X, Y = map(int, input().split())
mod = 1000000007

# xの階乗で随時あまりを取る
x_fact = [1]
for i in range(1, X+1):
    nex = x_fact[-1] * i % mod
    x_fact.append(nex)
# yの階乗で随時あまりを取る
y_fact = [1]
for i in range(1, Y+1):
    nex = y_fact[-1] * i % mod
    y_fact.append(nex)
# x+yの階乗で随時あまりを取る
xy_fact = [1]
for i in range(1, X+Y+1):
    nex = xy_fact[-1] * i % mod
    xy_fact.append(nex)
# 割り算なので逆元を求める
ans = xy_fact[-1] * pow(x_fact[-1], mod-2, mod) * pow(y_fact[-1], mod-2, mod) % mod
print(ans)