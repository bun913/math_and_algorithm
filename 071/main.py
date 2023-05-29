"""
全ての1次方程式の交点を求める
その交点のx,y座標を足し合わせて最大のものとのなるのが答え
"""
from itertools import combinations

def check_heikou(a1, b1, c1, a2, b2, c2):
    det = a1 * b2 - a2 * b1
    if det == 0:
      return False
    return True

def intersection(a1, b1, c1, a2, b2, c2):
    det = a1 * b2 - a2 * b1
    x = (b2 * c1 - b1 * c2) / det
    y = (a1 * c2 - a2 * c1) / det
    y = (a1 * c2 - a2 * c1) / det
    return x, y

N = int(input())
L = [tuple(map(int, input().split())) for _ in range(N)]

ans = -1
for comb in combinations(L, 2):
    a1, b1, c1 = comb[0][0], comb[0][1], comb[0][2]
    a2, b2, c2 = comb[1][0], comb[1][1], comb[1][2]
    # 交点
    check = check_heikou(a1, b1, c1, a2, b2, c2)
    if check is False:
        continue
    px, py = intersection(a1, b1, c1, a2, b2, c2)
    # 座標がNの一次方程式全てを満たしているかチェック
    check2 = True
    for i in range(N):
        a = L[i][0]
        b = L[i][1]
        c = L[i][2]
        if a * px + b * py > c:
            check2 = False
            break
    if check2 is False:
        continue
    ans = max(px + py,ans)
print(ans)