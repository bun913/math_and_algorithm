"""
フィボナッチ数列を求めるのだけどNが10**18であるため、
O(N)のアルゴリズムでは間に合わない。
フィボナッチ数列の性質を利用してO(logN)で求める。
フィボナッチ数列の性質として
A = [[1,1],[1,0]]とするとA**N-1の2行目の総和が答えになる。
"""
from copy import deepcopy

N = int(input())
mod = 10**9
A = [[1,1],[1,0]]
# まず2*2の行列の掛け算を実行する関数を定義する

def mul(A,B):
    # 2*2の行列の受け皿になる行列Cを初期化
    C = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
                C[i][j] %= mod
    return C

# 次に行列のN乗を求める関数を定義する
def pow(A,N):
    # ただし問題の性質から2**60まで計算すれば十分
    P = deepcopy(A)
    Q = [[0,0],[0,0]]
    flag = False
    for i in range(60):
        if N & 1<<i:
            if flag:
                Q = mul(Q,P)
            else:
                Q = deepcopy(P)
                flag = True
        P = deepcopy(mul(P,P))
    return Q
B = pow(A,N-1)
ans = (B[1][0] + B[1][1]) % mod
print(ans)