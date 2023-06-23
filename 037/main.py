"""
2つの線分が交差するかどうかを判定する
- ABが点Cと点Dを分ける（上と下に）
- CDが点Aと点Bを分ける（左と右に）
"""
# 2つのベクトルの内積
def cross(ax, ay, bx, by):
    return ax * by - ay * bx

X1, Y1 = list(map(int, input().split()))
X2, Y2 = list(map(int, input().split()))
X3, Y3 = list(map(int, input().split()))
X4, Y4 = list(map(int, input().split()))

ab_ac = cross(X2 - X1, Y2 - Y1, X3 - X1, Y3 - Y1)
ab_ad = cross(X2 - X1, Y2 - Y1, X4 - X1, Y4 - Y1)
cd_ca = cross(X4 - X3, Y4 - Y3, X1 - X3, Y1 - Y3)
cd_cb = cross(X4 - X3, Y4 - Y3, X2 - X3, Y2 - Y3)

# すべて一直線になっているコーナーケース
if ab_ac == 0 and ab_ad == 0 and cd_ca == 0 and cd_cb == 0:
    A = (X1, Y1)
    B = (X2, Y2)
    C = (X3, Y3)
    D = (X4, Y4)
    if A > B:
        A, B = B, A
    if C > D:
        C, D = D, C
    if max(A,C) <= min(B,D):
        print("Yes")
    else:
        print("No")
    exit()

isAB = ab_ac * ab_ad <= 0
isCD = cd_ca * cd_cb <= 0
if isAB and isCD:
    print("Yes")
else:
    print("No")
