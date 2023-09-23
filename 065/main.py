"""
市松模様に塗れば簡単にわかりそう
最初のコマと同じ模様の色になるマスの数を数える
ただし、H,Wが1の場合もあるのでそれはエッジケースとなる
"""
H, W = list(map(int, input().split()))
if H == 1 or W == 1:
    print(1)
    exit()
ans = (H * W) // 2 + (H * W) % 2
print(ans)