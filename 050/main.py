"""
a**bを1000000007で割った余りを求めよ
繰り返し二乗法で実装する
指数を2の累乗の積に分解する
"""

def mod_pow(a,n,mod):
    """
    繰り返し二乗法で実装している
    指数を2進数に変換している
    変換した結果桁が1になっているところの積を求めている
    """
    e = n
    base = a
    result = 1
    while e > 0:
        if e % 2 == 1:
            result *= base
            result %= mod
        base *= base
        base %= mod
        e //= 2
    return result

a, b = map(int, input().split())
print(mod_pow(a, b, 1000000007))