"""
一次元の表で管理できるかも
i番目の要素はi日目におけるとりうる最高の実力とする
でiの取りうる値は以下の2通りのどれか
- max(i-1番目の要素, i-2番目の要素+A[i])
"""
N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    a = A[i-1]
    if i == 1:
        dp[i] = a
        continue
    dp[i] = max(dp[i-1], dp[i-2]+a)
print(dp[-1])