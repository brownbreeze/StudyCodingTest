'''
타인의 답.
나는 python으로는 시간초과가 났다.
늘 시간초과가날 때, pypy를 쓸 순 없기 때문에, 시간초과 포인트를 찾아 고치자.
'''
import sys
import math


def is_goldbach_true(x):
    global primes
    for i in range(3, x//2+1, 2):
        if primes[i] and primes[x-i]:  # primes[i] = True if i is prime
            sys.stdout.write('%d = %d + %d\n' % (x, i, x-i))
            return True
    sys.stdout.write('Goldbach\'s conjecture is wrong.\n')
    return False


primes = [True] * (1000000+1)
primes[0] = False
primes[1] = False
for i in range(2, int(math.sqrt(1000000+1))+1):
    if primes[i]:
        for j in range(2*i, 1000000+1, i):
            primes[j] = False

n = int(sys.stdin.readline())
while n != 0:
    is_goldbach_true(n)
    n = int(sys.stdin.readline())
