"""
頂点1からKまで最短経路を出力する。
移動不可能な場合は-1を出力する。

これぞ幅優先探索の問題って感じ
"""
from collections import deque

N,M = map(int, input().split())

# グラフを作成
G = [list() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
q = deque([0])

ans = [-1 for _ in range(N)]
ans[0] = 0
while q:
    pos = q.popleft()
    for nex in G[pos]:
        if ans[nex] == -1:
            q.append(nex)
            ans[nex] = ans[pos] + 1
print(*ans, sep="\n")