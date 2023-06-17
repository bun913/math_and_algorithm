"""
今回の条件をちゃんと整理すると
A1,A2,...,ANは全て異なる。さらに全部0以上の整数（マイナスはない）
B1,B2,...,BNは全て異なる。さらに全部0以上の整数（マイナスはない）
てことはAiからBiを選ぶにあたって個々の最適はバッティングしない
なのでA1...から順に最適な経路をとっていけば良いだけ
もっというとAとBをソートしてそれぞれの値を取るだけ
"""
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ad = sorted(A)
bd = sorted(B)

ans = 0
for i in range(N):
    a = ad[i]
    b = bd[i]
    ans += abs(a-b)
print(ans)