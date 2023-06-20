"""
グラフだけどNが10**6とかなりでかい
"""
from collections import deque
N = int(input())
# グラフの作成
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
# 距離を格納する
dist = [-1] * N
dist[0] = 0
q = deque([0])
# 深さ優先探索をする
ans = 0
while q:
    pos = q.popleft()
    for nex in G[pos]:
        # 訪問済みである場合はスキップ
        if dist[nex] != -1:
            continue
        q.append(nex)
        dist[nex] = dist[pos] + 1
        ans += dist[pos] + 1
# 答えを求める
print(ans)