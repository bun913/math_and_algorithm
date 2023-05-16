"""
N個の整数の最大公約数を求める
Nが10**5,でAが10**18なので普通に1から数え上げると間に合わない
よってユークリッドの互助法を用いて1個のGCDをlogNで求める
N*logNで求めることができる
"""
from functools import reduce

def my_gcd(l:int, r:int) -> int:
    a = l
    b = r
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        if a == 0:
            return b
        if b == 0:
            return a

N = int(input())
A = list(map(int, input().split()))

ans = reduce(my_gcd, A)
print(ans)