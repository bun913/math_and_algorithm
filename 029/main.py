"""
これも動的計画法で解ける
N段目までに至るまでのそれぞれの段数を求めていけば良い
"""
N = int(input())
dp = [-1 for _ in range(N+1)]
dp[0] = 1
dp[1] = 1

for i in range(2,N+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[N])