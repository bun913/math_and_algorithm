"""
a,b,c,d
境界値を考える
"""
a,b,c,d = list(map(int, input().split()))
ans = max(a*c, a*d, b*c, b*d)
print(ans)