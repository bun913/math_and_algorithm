"""
N個の整数A1,A2,...,ANが与えらる。
1個以上の整数を選ぶ組み合わせは2**N-1通りある。
1個以上の整数を選んだ時の、「選んだ整数の最大値」を全て足した値
を1000000007で割ったあまりを求める。
"""
N = int(input())
A = list(map(int, input().split()))
MOD = 1000000007
power = [0 for _ in range(N)]
power[0] = 1
# べき乗の計算はこれがいちばん早いみたい
for i in range(1, N):
    power[i] = (power[i-1] * 2) % MOD

ans = 0
for i,a in enumerate(A):
    cnt = a * power[i]
    ans += cnt
    ans %= MOD
print(ans)