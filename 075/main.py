"""
足し算ピラミッドの問題を一般化したもの
Nが200,000と大きいので愚直に計算すると間に合わない
左からi番目の数字をa_iとして、それが足される回数を考える
a_iが足される回数はn-1Ciとなる
"""

class ModuloComb:
  def __init__(self, mod, num_factorial):
      self.mod = mod
      self.factorial = [ None ] * (num_factorial + 1) # factorial[i] = i! % mod
      self.factorial[0] = 1
      for i in range(1, num_factorial + 1):
          self.factorial[i] = self.factorial[i - 1] * i % self.mod
  
  def comb(self, n, r):
      return self.moddiv(self.factorial[n], self.factorial[r] * self.factorial[n - r] % self.mod)
  
  def moddiv(self, a, b): # (a / b) % mod
      return (a * self.modpow(b, self.mod - 2)) % self.mod
  
  def modpow(self, a, b):
      p = a
      answer = 1
      for i in range(30):
          if (b & (1 << i)) != 0:
              answer = (answer * p) % self.mod
          p = (p * p) % self.mod
      return answer

N = int(input())
MOD = 10**9 + 7
A = list(map(int, input().split()))

ans = 0
combo_module = ModuloComb(MOD, N - 1)
for i,a in enumerate(A):
    cnt = combo_module.comb(N-1,i)
    ans += a * cnt % MOD
print(ans % MOD)