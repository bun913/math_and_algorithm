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

その他
https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785
"""

# ユークリッドの互助法で最大公約数を求める
# a,bの長さの長方形をその時のいちばん大きい数で切り出していくイメージ

a, b = list(map(int, input().split()))

def max_common_vis(a:int, b:int) -> int:
    # ベースケース
    # もう切り出せない正方形になったら終了
    if b == 0:
        return a
    big = a if a >= b else b
    little = b if a >= b else a
    mod = big % little
    return max_common_vis(little, mod)

print(max_common_vis(a, b))
