"""
無向グラフで全ての頂点が連結であるか確認する
"""
from collections import deque

N, M = map(int, input().split())
# グラフを用意
G = [list() for _ in range(N)]

for _ in range(M):
    a,b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
# 実態はスタックとして扱う
q = deque([0])

visited = [False for _ in range(N)]
while q:
    pos = q.popleft()
    visited[pos] = True
    for nex in G[pos]:
        if visited[nex] is False:
            q.appendleft(nex)
if all(visited):
    print("The graph is connected.")
    exit()
print("The graph is not connected.")