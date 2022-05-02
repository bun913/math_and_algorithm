"""
Atcoderの問題解く用

1行1列データ

# str型で受け取るとき
s = input()
# int型で受け取るとき
s = int(input())
# float型　(小数)で受け取るとき
s = float(input())

(1,N)行列データ
s = input().split()
# listで整数で受け取る
l = list(map(int, input().split()))

その他
https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785
"""
import math

n = int(input())


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    sqr = math.floor(math.sqrt(n))
    for i in range(2, sqr):
        if n % i == 0:
            return False
    return True

result="Yes"
if not is_prime(n):
    result="No"
print(result)
