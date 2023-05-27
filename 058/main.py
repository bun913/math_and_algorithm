"""
"""
N, X, Y = list(map(int, input().split()))

abs_dist = abs(X) + abs(Y)
cond1 = abs_dist <= N
cond2 = N % 2 == abs_dist % 2

if cond1 and cond2:
    print('Yes')
    exit()
print('No')