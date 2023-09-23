"""
ますをX,Yに移動させるには
(i,j)から(i+1,j+2)の移動をa回
(i,j)から(i+2,j+1)の移動をb回とする。
X座標の制約: a + 2b = X
Y座標の制約: 2a + b = Y
を満たす。
連立方程式でとくと以下の様になる。
a = (2Y - X) / 3
b = (2X - Y) / 3
あとはa,bの移動をコンビネーションで解けば良いやつ
"""
X, Y = map(int, input().split())
mod = 10 ** 9 + 7
# a,bが負の数になってしまう
if (2 * Y -X) < 0 or (2 * X - Y) <0:
    print(0)
    exit()
# a,bが整数でない
if (2 * Y - X) % 3 != 0 or (2 * X - Y) % 3 != 0:
    print(0)
    exit()
# 全体の移動回数
# X座標の移動回数
tox = (2*Y - X) // 3
toy = (2*X - Y) // 3
al = tox + toy
# 全体の回数の階乗 // X座標の移動回数の階乗 // Y座標の移動回数の階乗 % mod
bunshi = 1
for i in range(1, al+1):
    bunshi *= i
    bunshi %= mod
bunbo = 1
for i in range(1, tox+1):
    bunbo *= i
    bunbo %= mod
for i in range(1, toy+1):
    bunbo *= i
    bunbo %= mod
# 逆元で答えを求める
ans = bunshi * pow(bunbo, mod-2, mod) % mod
print(ans)