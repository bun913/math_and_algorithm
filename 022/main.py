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
import math

def combination(n: int, r:int) -> int:
    if n == 0 or r == 0:
        return 0
    child = math.factorial(n)
    mother = math.factorial(r) * math.factorial(n-r)
    return child // mother
# 20万マイのカードから任意の二枚を選ぶ
# 1の場合99,999との組み合わせ
# 2の場合99,998との組み合わせとパターンは必ず決まっている
# なのでそれぞれの場合の和を求めていき最後に合計していけば良い

n = int(input())
l = list(map(int, input().split()))

# まずそれぞれの数が何枚あるかをdictに入れておく
## 辞書の初期化
d = {}
for n in range(1,100_000):
    d[n] = 0

## dictに格納していく
for num in l:
    d[num] += 1

## 50,000以下の場合の数を求める
ans = 0
for n in range(1,50000):
    remain = 100_000 - n
    ans += d[n] * d[remain]
## 50,000の場合の数を求める
combi = (d[50_000] * (d[50_000] - 1)) // 2
ans +=  combi
### combinationの数を求める
print(ans)
