"""
N*Nのますを考える
マス目を市松模様で塗り分けた時に白と黒のマスの目の数が同じにならないと無理
"""
N = int(input())
if N % 2 == 0:
    print("Yes")
    exit()
print("No")