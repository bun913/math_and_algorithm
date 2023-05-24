"""
品物の数Nが100まであるので全ての組み合わせを試すのは難しい
求めるもの: ナップサックの容量Wに入るだけのものを入れて価値の合計を最大化する
"""
N, W = map(int, input().split())
w = [0]
v = [0]
for _ in range(N):
    w_i, v_i = map(int, input().split())
    w.append(w_i)
    v.append(v_i)
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(W+1):
        # 今のマスの重さがi番目の品物より軽い場合は新しい品物を入れられない
        if j < w[i]:
            # 上の行から結果を引き継ぐのみ
            dp[i][j] = dp[i-1][j]
            continue
        # 新しい品物を入れる場合と入れない場合の価値を比較 
        cand1 = dp[i-1][j]
        cand2 = dp[i-1][j-w[i]] + v[i]
        dp[i][j] = max(cand1, cand2)
print(dp[N][W])