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
# これも期待値の線形性を利用して溶ける
# A時間勉強する確率は 1/3
# B時間勉強する確率は 2/3
# これを利用して期待値を算出する
# 計算はNで住むため10**6でも全然間に合うかと思う

n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

ans = 0.0
for i in range(0,n):
    ans += (al[i] * 1 / 3) + (bl[i] * 2/ 3)
print(ans)
