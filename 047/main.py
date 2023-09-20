"""
二部グラフかどうかを判定する
実際に幅優先探索で色を塗っていく
"""
from collections import deque

# 入力を受け取る
N, M = map(int, input().split())
G = [[] for _ in range(N)]  # グラフを表現する隣接リスト
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
color = [0] * N
# colorは0:未訪問, 1:グループA, 2:グループB
for v in range(N):
    # 訪問済みはスキップ
    if color[v] != 0:
        continue
    # 幅優先探索を行う
    q = deque([v])
    while q:
        qv = q.popleft()
        for nex in G[qv]:
            # 未訪問の場合は色を塗る
            if color[nex] == 0:
                next_color = 2 - color[qv]
                color[nex] = next_color
                q.append(nex)
                continue
            # 訪問済みの場合は色が同じであれば即終了
            if color[qv] == color[nex]:
                print("No")
                exit()
print("Yes")