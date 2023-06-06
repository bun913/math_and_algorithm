"""
2次元平面上のN個の点で最も近い2つの点の距離を求める
Nが2000なのでコンビネーションで求めても大丈夫そう
"""
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')
for i in range(N):
    for j in range(i+1, N):
        x1, y1 = points[i]
        x2, y2 = points[j]
        dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        ans = min(ans, dis)
print(ans)