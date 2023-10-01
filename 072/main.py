"""
整数A,Bが与えられる
x,yを A <= x < y <= B を満たす整数とする
gcd(x,y)の最大値を求める
考察
最大公約数の方を固定して、全探索してみる.gとする
x,yの値が存在するためにはA以上B以下の整数の中にgの倍数が2以上存在する必要がある
・つまりA以上B以下の倍数の数を求める小問題に帰着できる
・求め方は、B以下のgの倍数の数 - A-1以下のgの倍数の数
x,yが満たしている条件はA以上B以下の
"""
A,B = list(map(int, input().split()))

ans = 0
for g in range(1,B+1):
    a_mul_cnt = (A-1) // g
    b_mul_cnt = B // g
    if b_mul_cnt - a_mul_cnt >= 2:
        ans = max(ans, g)
print(ans)