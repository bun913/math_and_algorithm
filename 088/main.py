"""
3つの整数A,B、Cが与えられる
(1,2,...A) * (1,2,..,B) * (1,2,...,C)という式に置き換えられる
"""
A, B, C = list(map(int, input().split()))
mod = 998244353
a = (1 + A) * A // 2 % mod
b = (1 + B) * B // 2 % mod
c = (1 + C) * C // 2 % mod
ans = a * b * c % mod
print(ans)
