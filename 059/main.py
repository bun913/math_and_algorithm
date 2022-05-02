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

# まず以下のように考える
# 普通に計算して1のくらいの桁を導出すれば良いのでは
# でもそこでNが10**12までとりうるということに着目
# 1秒以内で計算するのは厳しいと確認
# そこで具体的に考えてみる
# n = 1 2, n=2 4, n=3 8, n=4 6
# n=5, 2, n=6 4, n=8 8, n=9 6
# これを繰り返すことがわかる

n = int(input())

ans = 0

if n % 4 == 0:
    ans = 6
elif n % 4 == 3:
    ans = 8
elif n % 4 == 2:
    ans = 4
elif n % 4 == 1:
    ans = 2

print(ans)
