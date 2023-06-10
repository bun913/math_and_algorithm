"""
V1..Vkのいずれかの倍数であるものの個数
包除原理で個数を数え上げれば解けそう
組み合わせはbit全探索で作ればなんとかんる
"""
from itertools import product
from functools import reduce
from math import gcd

def lcm(*numbers):
    return reduce(lambda x, y: (x * y) // gcd(x, y), numbers, 1)

N, K = list(map(int, input().split()))
V = list(map(int, input().split()))

ans = 0
for pro in product((0,1), repeat=K):
    # 1個以上の数値を使う
    if sum(pro) == 0:
        continue
    tmp = []
    for j in range(K):
        if pro[j] == 1:
            tmp.append(V[j])
    mul = lcm(*tmp)
    quto = N // mul
    # 包除原理では使っている数の個数が2の倍数の時は引く、2の倍数じゃない時は足す
    if sum(pro) % 2 == 0:
        ans -= quto
        continue
    ans += quto
print(ans)