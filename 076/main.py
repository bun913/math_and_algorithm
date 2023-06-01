"""
足される数を考える問題
絶対値というのがポイントで配列を大きい順に並び替えても結果は同じ
単純に書く項目の足される数を考えて一般化した式を作れば良いだけ
"""

N = int(input())
A = list(map(int, input().split()))
ad = sorted(A, reverse=True)
ans = 0

for i in range(N):
    cnt = (N-2*i-1) * ad[i]
    ans += cnt
print(ans)