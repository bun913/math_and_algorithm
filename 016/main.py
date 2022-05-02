"""
Atcoderの問題解く用

1行1列データ

#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())
#float型　(小数)で受け取るとき
s = float(input())

(1,N)行列データ
s = input().split()
# listで整数で受け取る
l = list(map(int, input().split()))

その他
https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785
"""

def gcd(a: int, b: int) -> int:
    small = b if a > b else a
    big = a if a > b else b
    if small == 0:
        return big
    return gcd(big % small, small)

n = input()
l = list(map(int, input().split()))
# 計算
ans = gcd(l.pop(), l.pop())
for i in range(2, len(l)):
    ans = gcd(ans, l.pop())
print(ans)
