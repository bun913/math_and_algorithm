"""
賞金の期待値を求める
それぞれ個々の事象の期待値の和が和の期待値になる
"""
N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

b = sum(B) / N
r = sum(R) / N
ans = b + r
print(ans)