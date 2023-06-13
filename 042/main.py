"""
エラストテネスのふるいのようにf(i)を計算する
"""
N = int(input())
f_list = [0 for _ in range(N+1)]
for i in range(1, N+1):
    # iの倍数
    for j in range(i, N+1,i):
        f_list[j] += 1
ans = 0
for i in range(1, N+1):
    ans += i*f_list[i] 
print(ans)