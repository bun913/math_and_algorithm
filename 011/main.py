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
def _is_prime(i: int) -> bool:
    count = 0
    result = True
    for n in range(1 ,i+1):
        if count > 2:
            result = False
            break
        if i % n == 0:
            count += 1
    if count > 2:
        result = False
    return result

n = int(input())
l = [ str(i) for i in range(2, n+1) if _is_prime(i) ]
print(" ".join(l))
