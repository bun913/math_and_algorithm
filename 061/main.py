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
# Nこの時に勝ち、負けとなる状態を考える

n = int(input())
ans = "First"
flg = False

for i in range(1,60):
    if n == (2 ** i) - 1:
        flg = True
        break

if flg:
    ans = "Second"

print(ans)
