from collections import Counter

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)
ans = 0
for i in range(1, 50_001):
    if i == 50_000:
        ans += C[i] * (C[i]-1) // 2
        continue
    ans += C[i] * C[100_000-i]
print(ans)