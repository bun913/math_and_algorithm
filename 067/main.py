"""
まずH行の和を配列hsumに格納する
次のW列の和をそれぞれ配列wsumに格納する
"""
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
hsum = [0] * H
for i in range(H):
    hsum[i] = sum(A[i])
wsum = [sum(col) for col in zip(*A)]
for i in range(H):
    row = []
    for j in range(W):
        col = hsum[i] + wsum[j] - A[i][j]
        row.append(col)
    print(*row)