from collections import deque

R, C = map(int, input().split())
sx, sy = map(int, input().split())
sx -= 1
sy -= 1
gx, gy = map(int, input().split())
gx -= 1
gy -= 1
maze = [list(input()) for _ in range(R)]

G = [[] for _ in range(R*C)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# グラフを作成
for i in range(R):
    for j in range(C):
        if maze[i][j] == '#':
            continue
        idx1 = i*C + j
        for dx, dy in dxy:
            idx2 = (i+dx)*C + (j+dy)
            if 0 <= i+dx < R and 0 <= j+dy < C and maze[i+dx][j+dy] == '.':
                G[idx1].append(idx2)
                G[idx2].append(idx1)
# 幅優先探索でスタートからゴールの最短距離を求める
start = sx*C + sy
goal = gx*C + gy
q = deque([start])
dist = [-1] * (R*C)
dist[start] = 0

while q:
    cur = q.popleft()
    for nex in G[cur]:
        # 訪問済みはスキップ
        if dist[nex] != -1:
            continue
        dist[nex] = dist[cur] + 1
        q.append(nex)

ans = dist[goal]
print(ans)
