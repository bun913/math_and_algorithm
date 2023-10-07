"""
N人家族
A1 B1
A2 B2
A3 B3
の人とそれぞれMax一歳差
"""
from collections import deque
# 条件の入力
N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]
# AとBからグラフを作成する
for _ in range(M):
    a, b = list(map(int, input().split()))
    G[a-1].append(b-1)
    G[b-1].append(a-1)
# グラフの頂点同志の差が1以下ということは自明
# つまり、各頂点までの最大距離を求めて、最後の頂点までの最大距離を出力すれば良い
# キューを使って幅優先探索で求めれる
dis = [-1] * N
dis[0] = 0
q = deque([0])
while q:
    cur = q.popleft()
    for nex in G[cur]:
        if dis[nex] == -1:
            # 距離を更新して、キューに追加
            dis[nex] = dis[cur] + 1
            q.append(nex)
for d in dis:
    # 頂点1から到達できない場合はMax値として120を出力
    if d == -1:
        print(120)
        continue
    print(d)