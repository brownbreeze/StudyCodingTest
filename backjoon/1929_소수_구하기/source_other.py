import math
M, N = map(int, input().split())

Sieve = [True for i in range(N + 1)]
Sieve[0] = False
Sieve[1] = False

for i in range(2, math.floor(N ** 0.5) + 1):
    if Sieve[i]:
        a = 2 * i
        while a <= N:
            Sieve[a] = False
            a += i

for i in range(M, N + 1):
    if Sieve[i]:
        print(i)
