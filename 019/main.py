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
# コンビネーションの n r を利用すれば良い
# n! / r!(n-r)!がコンビネーション

import math

def facto(num: int) -> int:
    return math.factorial(num)

n = int(input())
l = list(map(int, input().split()))

r_count = l.count(1)
y_count = l.count(2)
b_count = l.count(3)

# それぞれの色から2つを選ぶ組み合わせの数を算出
r_combi = r_count * (r_count-1) / 2
y_combi = y_count * (y_count-1) / 2
b_combi = b_count * (b_count-1) / 2
print(int(r_combi + y_combi + b_combi))
