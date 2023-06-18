# 素数の数え上げ
# 普通に数え上げても間に合う
from math import sqrt

# 数え上げバージョン
def is_primse(n: int) -> bool:
    # nは2以上の整数とする
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

N = int(input())
ans = []
for i in range(2,N+1):
    if is_primse(i):
        ans.append(i)
print(*ans)
