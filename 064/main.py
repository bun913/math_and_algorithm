"""
数列の数の絶対値を求める
まずその絶対値がKの値を超える場合は無理
またKの方が大きくても、偶奇が合わないと無理
ちょうどK回操作しないといけないから
"""
from functools import reduce

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

abs_sum = reduce(lambda bef, cur: bef + abs(cur), A, 0)
if abs_sum > K:
    print('No')
    exit()
if abs_sum % 2 != K % 2:
    print('No')
    exit()
print("Yes")