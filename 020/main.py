"""
N枚のカード
Aiがi番目
5枚選ぶ方法のうち、整数の和がちょうど100となるものの通り数
Nが100なので 100C5で75287520で10**7くらい
ギリギリ間に合うかも
"""
N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            for l in range(k+1, N):
                for m in range(l+1, N):
                    if A[i]+A[j]+A[k]+A[l]+A[m] == 1000:
                        ans += 1
print(ans)