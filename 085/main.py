"""
"""
N, X, Y = map(int, input().split())
if Y > N ** 4:
    print("No")
    exit()
# Yの約数を列挙する
divisors = []
for i in range(1, N + 1):
    if Y % i == 0:
        divisors.append(i)
for i in range(len(divisors)):
    for j in range(i,len(divisors)):
        for k in range(j,len(divisors)):
            for l in range(k,len(divisors)):
                if divisors[i] + divisors[j] + divisors[k] + divisors[l] == X:
                    print("Yes")
                    exit()
print("No")