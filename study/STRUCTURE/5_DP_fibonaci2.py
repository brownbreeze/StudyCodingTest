# 피보나치 수열 문제를 bottom up
memo = {1:1, 2:1}

def fibo(n):
    for i in range(3, n+1):
        print(f'fibo {i}')
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

print(fibo(7))
'''
fibo 3
fibo 4
fibo 5
fibo 6
fibo 7
13
'''