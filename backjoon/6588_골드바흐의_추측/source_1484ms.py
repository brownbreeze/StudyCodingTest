import math
import sys
#             sys.stdout.write('%d = %d + %d\n'%(x, i, x-i))
#             return True
#     sys.stdout.write('Goldbach\'s conjecture is wrong.\n')
max = 1000000
m = [True for i in range(max+1)]  # 해당 값의 약수의 합 f(x)를 담는 메모

m[1] = False

for i in range(2, 1000001):
    if not m[i]:
        continue  # 2를 이전에 했다면, 4를 지나칠 수 있게
    for j in range(i*2, 1000001, i):
        m[j] = False  # 소수가 아니야


def solution(n):
    global m
    for i in range(3, n//2+1, 2):
        # print(n, i, n-i)
        if not m[i]:
            continue
        if not m[n-i]:
            continue
        print(f"{n} = {i} + {n-i}")
        return 0
    print("Goldbach's conjecture is wrong.")
    return 0


n = int(sys.stdin.readline())
while n != 0:
    solution(n)
    n = int(sys.stdin.readline())
