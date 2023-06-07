"""
N文字の`(`か`)`からなる文字列Sが与えられる。
Sが正しいかっこ文字列か判定する。
これもいきなり正解を導き出そうとせずに、動的計画法みたいにn文字目までが正しいかっこ列かを考える
- n文字目までに登場する(の数が)の数以上であること
- 最終的に(の数と)の数が同じであること
と求められる
"""
N = int(input())
S = input()
l_cnt = 0
r_cnt = 0

for s in S:
    if s == "(":
        l_cnt += 1
    else:
        r_cnt += 1
    if l_cnt < r_cnt:
        print("No")
        exit()
if l_cnt == r_cnt:
    print("Yes")
else:
    print("No")