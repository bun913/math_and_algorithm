"""
動的計画法で解ける
オーブンAに入れる料理の総和が決まれば、オーブンBで入れる料理の総和も決まる
つまりAだけ考えれば良いわけだが、どのような料理の時間を実現できるかという動的計画法を考える
dp[i][j] := i番目までの料理を使って、j分以内に実現できる最大の時間
"""
N = int(input())
T = list(map(int, input().split()))
s = sum(T)
# 動的計画法。実現できる料理の最大はsまでなので
dp = [ [False for _ in range(s+1)] for _ in range(N+1)]
dp[0][0] = True
# 動的計画法の準備
for i in range(1, N+1):
    t = T[i-1]
    for j in range(s+1):
        # この料理を使わなくても実現できる
        if dp[i-1][j] is True:
            dp[i][j] = True
        # この料理を使う場合
        # またtを使える時間に到達していない場合はスキップ
        if t > j:
            continue
        if dp[i-1][j-t] is True:
            dp[i][j] = True
# 動的計画法を再度みて、AとBの合計時間がいい感じ（最小）になるものを探す
ans = float('inf')
for i in range(N+1):
    for j in range(s+1):
        if dp[i][j] is False:
            continue
        a = j
        b = s - j
        ans = min(ans, max(a,b))
print(ans)