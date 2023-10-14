"""
L以上R以下の素数の個数を求めるというやつ
これはエラストテネスの古いを使えば解けるのではないか
Rは10**12と大きいが、制約でR-Lはせいぜい500,000であることがわかっている
"""
L , R = map(int,input().split())
# R-L+1の配列を作る
primes = [True for _ in range(R-L+1)]
if L == 1:
    primes[0] = False

# かける数をaとする
LIMIT = int(R**0.5)
for a in range(2,LIMIT+1):
    min_value = ((L+a-1)//a) * a
    for b in range(min_value, R+1, a):
        if b == a:
            continue
        primes[b-L] = False
ans = 0
for p in primes:
    if p is True:
        ans += 1
print(ans)