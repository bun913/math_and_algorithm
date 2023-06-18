# あえてpermutationsを使わずに解いてみる
from functools import reduce

N = int(input())
ans = reduce(lambda bef, now: bef * now, range(1, N + 1))
print(ans)