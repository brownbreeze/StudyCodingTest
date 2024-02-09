# 피보나치 수열 문제를 top down 방식으로 사용됨
memo = {}

def fibo(n):
    if n == 1 or n == 2:
        print(f'fibo {n}')
        return 1
    if n not in memo:
        print(f'fibo {n}')
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

print(fibo(7))
'''
fibo 7
fibo 6
fibo 5
fibo 4
fibo 3
fibo 2
fibo 1
fibo 2
13
'''