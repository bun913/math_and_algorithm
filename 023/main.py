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

# 賞金の期待値を計算する
# 期待値の和が和の期待値になる法則を知らなければ全探索で確率と期待値を足し上げていく
# ↑今回はこの法則を利用して期待値を計算することができる

n = int(input())
bl = list(map(int, input().split()))
rl = list(map(int, input().split()))

ans = (sum(bl) / len(bl)) + (sum(rl) / len(rl))
print(ans)
