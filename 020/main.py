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

# まず場合の和を考える
# 最大100の中から5つの組み合わせを求める
# 全探索でやるとしたら1見nの5乗となって終わらない計算に見えそう
# でも冷静に数を求めると 100C5 となってたかだか 100*99*98*97*96 / 5!
# 10の18乗には遠く及ばない
# なので今回は全探索で解答できると見積もれる

n = int(input())
l = list(map(int, input().split()))

count = 0
for a in range(0,n):
    for b in range(a+1,n):
        for c in range(b+1,n):
            for d in range(c+1,n):
                for e in range(d+1,n):
                    total = l[a] + l[b] + l[c] + l[d] + l[e]
                    if  total == 1000:
                        count += 1

print(count)
