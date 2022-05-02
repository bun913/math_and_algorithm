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
import math

# 素因数分解
# Nの素因数分解をしていくにあたりルートNを超えるものはあっても一つ
# だってルートNを超えるものが2つあったらN超えるから
# ということでNの平方根までをforの対象とする


def prime_fuctorization(n: int) -> list:
    LIMIT = int(math.sqrt(n))
    # 2,3,4,5...のような形で割り算を続けていく
    l_ans = []
    for i in range(2, LIMIT+1):
        # iがNで割り切れれば答えに追加
        # 破り続ける限り破り続ける
        while n % i == 0:
            l_ans.append(i)
            n //= i
    # 最後2以上のものがあまりとしてある場合追加する必要がある
    # ex:10 / 2では5まで破り続けないので5を答えに追加する必要がある
    # 36のように最後まで平方根以下の素数で破り続けれる場合は必要なし
    if n >= 2:
        l_ans.append(n)
    return l_ans

n = int(input())
ans = prime_fuctorization(n)
print(*ans)
