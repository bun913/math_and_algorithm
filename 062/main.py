"""
テレポーターは絶対にどっかのタイミングでループするので
剰余の考えを使えばNの計算でいけそう
初めて訪れた時の手数をFirstという配列で記録
2回目に訪れた時の手数をSecondという配列で記録
"""
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

# 初期化
firsts = [-1 for _ in range(N+1)]
seconds = [-1 for _ in range(N+1)]
dist = {}
for i, a in enumerate(A):
    dist[i+1] = a

# 町1からスタート
cnt = 0
cur_town = 1
while True:
    # firstsの更新
    if firsts[cur_town] == -1:
        firsts[cur_town] = cnt
    # secondsの更新
    elif seconds[cur_town] == -1:
        seconds[cur_town] = cnt
    # ループに至る前に終了する場合
    if cnt == K:
        print(cur_town)
        exit()
    # ループに入って戻ってきている場合
    if firsts[cur_town] != -1 and seconds[cur_town] != -1:
        L = seconds[cur_town] - firsts[cur_town]
        if (K - firsts[cur_town]) % L == 0:
            print(cur_town)
            exit()
    cnt += 1
    cur_town = dist[cur_town]
