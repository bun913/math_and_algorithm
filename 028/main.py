N = int(input())
H = list(map(int, input().split()))
H.insert(0,0)
dp = [-1 for _ in range(N+1)]
dp[0] = 0
for i in range(1, N+1):
    if i == 1:
        dp[i] = 0
        continue
    if i == 2:
        dp[i] = abs(H[i]- H[i-1])
        continue
    c1 = dp[i-1] + abs(H[i]-H[i-1])
    c2 = dp[i-2] + abs(H[i]-H[i-2])
    dp[i] = min(c1, c2)
print(dp[-1])