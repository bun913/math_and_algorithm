"""
一見普通に計算すれば良いのだけどa,b,cがとても大きく、ルートを取るとオーバーフローしてしまう
なのでsqrt(a) + sqrt(b) < sqrt(c)という条件を満たすように変形する

"""
a, b, c = list(map(int, input().split()))
left = 4 * a * b
right = (c - a - b) ** 2
# c-a-bがマイナスになる時は絶対に条件を満たさない
if c - a- b < 0:
    print("No")
    exit()
if left < right:
    print("Yes")
    exit()
print("No")