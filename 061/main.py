"""
1,3,7,15という形で負けの状態がくる
"""
N = int(input())
# 紛らわしいので先に弾く
a = 1
while a <= N:
    if a == N:
        print("Second")
        exit()
    a *= 2
    a += 1
print("First")