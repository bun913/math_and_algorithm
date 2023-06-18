"""
a1=1,a2=1
an = 2 * an-1 + an-2
これのN項を10**9で割った余りを求める
Nが10**18でO(N)のアルゴリズムでは間に合わない
行列を使ってO(logN)で求める
"""
from copy import deepcopy

MOD = 10**9 + 7

# 2×2 行列 A, B の積を返す関数
def multiply(A, B):
	global MOD
	C = [ [ 0, 0 ], [ 0, 0 ] ]
	for i in range(2):
		for j in range(2):
			for k in range(2):
				C[i][j] += A[i][k] * B[k][j]
				C[i][j] %= MOD
	return C

# A の n 乗を返す関数
def power(A, n):
	P = deepcopy(A)
	Q = [ [ 0, 0 ], [ 0, 0 ] ]
	flag = False
	for i in range(60):
		if (n & (1 << i)) != 0:
			if flag == False:
				Q = deepcopy(P)
				flag = True
			else:
				Q = deepcopy(multiply(Q, P))
		P = deepcopy(multiply(P, P))
	return Q


N = int(input())
A = [[2,1],[1,0]]
ans_mat = power(A,N-1)
ans = (ans_mat[1][0] + ans_mat[1][1]) % MOD
print(ans)