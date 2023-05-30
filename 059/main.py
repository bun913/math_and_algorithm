"""
2**Nの一の位を求める
あくまでかけ続けるのは2で固定
つまり1の位はループする
2,4,8,6のループとなる
"""
N = int(input())

if N %4 == 1:
    print(2)
    exit()
elif N % 4 == 2:
    print(4)
    exit()
elif N % 4 == 3:
    print(8)
    exit()
print(6)