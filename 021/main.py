from math import factorial
# set max recursin depth 10 ** 9
import sys
sys.setrecursionlimit(10 ** 9)

def my_permutaion(n:int,r: int) -> int:
    return factorial(n) // factorial(n-r)

def my_combination(n:int, r:int) -> int:
    return my_permutaion(n, r) // factorial(r)

n, r = list(map(int, input().split()))
ans = my_combination(n, r)
print(ans)