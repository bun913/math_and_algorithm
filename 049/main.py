"""
フィボナッチ数列を計算していくわけだけど
Nが10**7と非常に大きいので、普通にやると桁数が大きくなりすぎる
フィボナッチ数列はいっても足し算でもとめていくので、計算の途中であまりをとっても結果は変わらない
"""
N = int(input())
fib = [1,1]# 最初の2項目は入れておく
for i in range(2,N):
    nex = fib[i-1] + fib[i-2]
    fib.append(nex%1000000007)
print(fib[N-1])