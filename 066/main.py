"""
そもそもの条件がorで繋がっていて候補数が多すぎる
と考えれば
赤を固定して
青と赤の差の絶対値がKより小さい
白と赤の差の絶対値がKより小さい
という条件を全て満たすものを数える
"""
N,K = list(map(int, input().split()))

ce = 0
# 赤の候補を固定してみる
for red in range(1, N+1):
    # 青は赤との差の絶対値がKより小さくなるように全探索
    for blue in range(red-K+1, red+K):
        if blue < 1 or blue > N:
            continue
        # 白は赤との差の絶対値がKより小さくなるように全探索
        for white in range(red-K+1, red+K):
            if white < 1 or white > N:
                continue
            if abs(blue-white) < K:
                ce += 1
ans = N * N * N - ce
print(ans)
