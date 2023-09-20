"""
グラフを作るのは問題ない
それぞれの頂点の中で自分自身より頂点番号が小さい隣接頂点が1つだけある頂点の数
"""
N, M = map(int, input().split())

# グラフを作成
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
# 判定
ans = 0
for i,g in enumerate(G):
    # 隣接頂点なし
    if len(g) == 0:
        continue
    sg = sorted(g)
    min_val = sg[0]
    # 要素が一つしかない
    if len(g) == 1:
        if min_val < i:
            ans += 1
        continue
    second_min = sg[1]
    if min_val < i and second_min > i:
        ans += 1
print(ans)