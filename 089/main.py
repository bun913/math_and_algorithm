"""
指数法則と式の変形で整数の世界に持ち込む
"""
a, b, c = list(map(int, input().split()))
# cが1の場合は、aとbの大小関係は問わない
if c == 1:
    print("No")
    exit()
v = 1
# 普通に c ** bを計算すると、オーバーフローする可能性がある
# 随時計算していってaを越えたら終了
for i in range(1,b+1):
    # a < (v * c)を言い換え
    if a // c < v:
        print("Yes")
        exit()
    v *= c
print("No")