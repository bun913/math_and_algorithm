N = int(input())
ans = 0

for i in range(N):
    p, q = map(int, input().split())
    expected = q / p
    ans += expected
print(ans)