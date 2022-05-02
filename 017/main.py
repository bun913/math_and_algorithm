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

# N個の最小公倍数を求める問題
# 最小公倍数を求めるには a * b / aとbの最大公約数

def max_divisor(a: int, b: int) -> int:
    small= b if a > b else a
    big = a if a > b else b
    # ベースケース
    if small == 0:
        return big
    return max_divisor(small, big % small)

def least_common(a:int, b:int) -> int:
    return (a * b) // max_divisor(a, b)

n = int(input())
l = list(map(int, input().split()))
a = l.pop()
b = l.pop()
ans = least_common(a,b)
for i in range(2, n):
    a = l.pop()
    ans = least_common(ans, a)
print(ans)
