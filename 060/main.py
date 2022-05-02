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
# 規則性を見つけるとあっさり解ける類の問題
# Nを実際に考えてみる1~3の場合先行が勝てる
# 4の場合は絶対後衛がかつ
# 5~7の場合は絶対に選考がかつ(4を後衛に撮らせれば良い)
# 8の場合は絶対に後攻がかつ
# 9~11の場合は絶対に先行がかつ(8・4を後衛にとらせればよい)

n = int(input())
ans = "First"
if n % 4 == 0:
    ans = "Second"
print(ans)
