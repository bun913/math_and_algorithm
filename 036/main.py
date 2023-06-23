"""
時計の短針と長針の先端同士の距離を求める
三角関数で解くことができる
長針の角度: 30H + 0.5M
短針の角度: 6M
時計の中心を(0,0)とした時各針の座標は求められる
長身の先端: (A * cos(30H + 0.5M), A * sin(30H + 0.5M))
短針の先端: (B * cos(6M), B * sin(6M))
"""
import math

A, B, H, M = list(map(int, input().split()))
# 長針の座標
x1 = A * math.cos(math.radians(30 * H + 0.5 * M))
y1 = A * math.sin(math.radians(30 * H + 0.5 * M))
# 短針の座標
x2 = B * math.cos(math.radians(6 * M))
y2 = B * math.sin(math.radians(6 * M))
# 二点間の距離を求める
ans = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(ans)