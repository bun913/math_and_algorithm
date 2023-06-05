"""
2次元平面乗に点A,B,Cがある。
点Aと線分BC乗の点の最短距離を求める。

まず、点A,B,Cのそれぞれのなす角の正負によってパターンが変わる
1. 角ABCが90度より大きい（BAとBCの内積が負）
2. 角ACBが90度より大きい（CAとCBの内積が負）
3. 1でも2でもないABCで鋭角三角形（BAとBCの内積が正、CAとCBの内積が正）ができる
"""
import math

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)

    # 内積
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # 外積
    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        length = self.length()
        if length != 0:
            self.x /= length
            self.y /= length

    def rotated(self, angle):
        rad = math.radians(angle)
        cos = math.cos(rad)
        sin = math.sin(rad)
        x = self.x * cos - self.y * sin
        y = self.x * sin + self.y * cos
        return Vector2D(x, y)

ax,ay = list(map(int, input().split()))
bx,by = list(map(int, input().split()))
cx,cy = list(map(int, input().split()))

v_ba = Vector2D(ax - bx, ay - by)
v_bc = Vector2D(cx - bx, cy - by)

# パターン1
if v_ba.dot(v_bc) < 0:
    # AとBの距離を出力
    print(v_ba.length())
    exit()
v_ca = Vector2D(ax - cx, ay - cy)
v_cb = Vector2D(bx - cx, by - cy)
# パターン2
if v_ca.dot(v_cb) < 0:
    # AとCの距離を出力
    print(v_ca.length())
    exit()
# パターン3
# 外積から平行四辺形の面積を求める
area = abs(v_ba.cross(v_bc))
# 平行四辺形の面積 // BCの長さ
ans = area / v_bc.length()
print(ans)