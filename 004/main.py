# import reduce
from functools import reduce
A = list(map(int, input().split()))
ans = reduce(lambda bef,a: bef * a, A)
print(ans)