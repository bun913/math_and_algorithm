"""
点とぶつからない長方形は満たさない
なぜなら点とぶつかることで、囲む点の数を変えずに面積を小さくすることができるから
Kはたかだが50なので、Kの点の最小値を取ることで、全探索できる
"""
from itertools import combinations

# 4点の座標の中にK点以上含まれるかどうかを判定する
def check_numpoints(N,X, Y, lx, rx, ly, ry):
    cnt = 0
    for i in range(N):
        if lx <= X[i] <= rx and ly <= Y[i] <= ry:
            cnt += 1
    return cnt >= K

N, K = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(N)]
X = [xy[i][0] for i in range(N)]
Y = [xy[i][1] for i in range(N)]

ans = float("inf")
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                cl,cr,dl,dr = X[i], X[j], Y[k], Y[l]
                # 長方形を作るためにcl < cr, dl < drである必要がある
                if cl < cr or dl < dr:
                    if check_numpoints(N,X,Y,cl,cr,dl,dr):
                        ans = min(ans, (cr-cl)*(dr-dl))
print(ans)