"""
Atcoderの問題解く用

1行1列データ

#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())
#float型　(小数)で受け取るとき
s = float(input())

(1,N)行列データ
s = input().split()
# listで整数で受け取る
l = list(map(int, input().split()))

その他
https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785
"""

n, k = list(map(int, input().split()))
l = list(map(int, input().split()))

# すでに１度訪れた街かを記憶する
town_mem = set()

# こいつの中にバグがある
def find_base_town(l:list, town_mem: set,town_num: int):
    # ベースケース
    if town_num in town_mem:
        return town_num
    town_mem.add(town_num)
    return find_base_town(l, town_mem,l[town_num-1])

# どこの街を起点に何回でその街に戻ってくるのかを調べる
base_town = find_base_town(l, town_mem, 1)
town_mem = set()
# 最初に起点の街に辿り着くまでに必要な回数
flg = True
cur = 1
ini_c = 0
while flg:
    # 終了条件
    if cur == base_town:
        flg = False
        break
    ini_c += 1
    cur = l[cur-1]

# ループのための回数
# 純粋にベースとなる街から２回目にその街に戻るまでのループ回数
base_count = 0
cur = 1
loop_count = 0
while base_count <= 1:
    if base_count == 1:
        loop_count += 1
    if cur == base_town:
        base_count += 1
    cur = l[cur-1]

# k回は最小何回テレポートしたのと同じなのか計算
# ループの回数で割理続ける
def calc(n:int, loop_count):
    # ベースケース
    mod = n % loop_count
    if mod >= loop_count:
        return calc(mod, loop_count)
    else:
        return mod

terepo_count = calc(k-ini_c, loop_count)

ans = 0
next_town = 1
for i in range(1, ini_c+terepo_count+1):
    next_town = l[next_town-1]

print(next_town)
