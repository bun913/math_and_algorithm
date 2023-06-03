"""
この場合映画に満足度などはなく単純に数をこなせば良い
であれば、貪欲法で今見れる映画で時間がいちばん早く終わるものを選び続ければOK
これをOlogNで実装するには、区間スケジューリング問題というものを利用する
あらけじめ終了時刻の早い時間順にソートしておく
"""
from operator import itemgetter

# 終了時刻が小さい順にidを並び替える
N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
lrd = sorted(LR, key=itemgetter(1))

# 終了時刻が早い順に見ていく
ans = 0
last = 0 # 前回の映画の終了時刻
for st,en in lrd:
    if last <= st:
        ans += 1
        last = en
print(ans)