"""
O(N)だと無理だけどO(logN)なら間に合うので、
a * bとなる整数を探索するけど、平方根まで探索すれば十分
"""
N = int(input())

ans = float('inf')
for a in range(1, int(N**0.5)+1):
   if N % a != 0:
       continue 
   b = N // a
   circ = 2 * a + 2 * b
   ans = min(ans, circ)
print(ans)