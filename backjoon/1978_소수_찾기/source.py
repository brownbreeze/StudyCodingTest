import math
c = int(input())
arr = map(int, input().split())

maxnum = 1000
Sieve = [True for i in range(1001)]
Sieve[0] = False
Sieve[1] = False

for i in range(2, math.floor(maxnum ** 0.5) + 1):
    if Sieve[i]:
        a = 2 * i
        while a <= maxnum:
            Sieve[a] = False
            a += i

result = 0
for num in arr:
    if Sieve[num]:
        result += 1
print(result)
