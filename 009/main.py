# 500点取得 全探索の場合

N, S = list(map(int, input().split()))
A = list(map(int, input().split()))
# ans = 0

# for p in product([0, 1], repeat=N):
#     s = 0
#     for i in range(N):
#         if p[i] == 1:
#             s += A[i]
#     if s == S:
#         print("Yes")
#         exit()
# print("No")

# 動的計画法の場合
# 2次元の表にしてカードを行がi枚目まで選んで良いものにする
# 横の軸をカードの数の合計として、その値を作れるかどうかをTrue/Falseで表す
dp = [[False for _ in range(S+1)] for _ in range(N+1)]
dp[0][0] = True

for i in range(1,N+1):
    a = A[i-1]
    for j in range(S+1):
        if j < a:
            dp[i][j] = dp[i-1][j]
            continue
        cond1 = dp[i-1][j] is True
        cond2 = dp[i-1][j-a] is True
        dp[i][j] = cond1 or cond2
        if j == S and dp[i][j] is True:
            print("Yes")
            exit()
print('No')