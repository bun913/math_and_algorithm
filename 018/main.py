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

# 与えられるものが100,200,300,400のうちのいずれかだけ
# そのうち2つを選んで500になるのは
# a: 100 , 400 と
# b: 200,300 の組み合わせだけ
# 100円の数 * 400円の数 + 200円の数 * 300円の数
n = int(input())
l = list(map(int, input().split()))

ab = l.count(100) * l.count(400)
cd = l.count(200) * l.count(300)
print(ab + cd)
