"""
"""
def gcd(a,b):
    # xを大きい方としたい
    x, y = a, b
    # ガードケース
    if x == 0 or y == 0:
        return max(x,y)
    if x <= y:
        x, y = y, x
    return gcd(y, x%y)

A, B = map(int, input().split())
g = gcd(A,B)
lcm = A * B // g
if lcm > 10 ** 18:
    print("Large")
    exit()
print(lcm)