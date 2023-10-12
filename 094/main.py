"""
Nこの整数からなる数列Aがあるが、値がわからない
BはN-1個の数列で値がわかっている
max(Ai, Ai+1) <= Biを満たしている
Aの合計としてありうる最大の値を求めよ

そのためAi,Ai+1は両方Bi以下
さらにAi+1,Ai+2は両方Bi+1以下
Ai+1の最大値はmin(Bi,Bi+1)である
"""
N = int(input())
B = list(map(int, input().split()))
A = [0] * N

for i in range(N):
    if i ==0:
        A[i] = B[i]
        continue
    if i == N-1:
        A[i] = B[i-1]
        continue
    A[i] = min(B[i-1], B[i])
print(sum(A))