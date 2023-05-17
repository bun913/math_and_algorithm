from functools import reduce

def my_gcd(l:int, r:int) -> int:
    a = l
    b = r
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        if a == 0:
            return b
        if b == 0:
            return a

def my_lcm(l:int, r:int) -> int:
    g = my_gcd(l, r)
    lcm = g * (l // g) * (r // g)
    return lcm

N = int(input())
A = list(map(int, input().split()))

ans = reduce(my_lcm, A)
print(ans)