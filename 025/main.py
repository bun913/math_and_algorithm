N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = sum(A)
b = sum(B) * 2
ans = (a+b) / 3
print(ans)