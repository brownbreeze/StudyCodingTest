def solution(n, money):
    answer = 0
    money.sort()
    while True:
        if money[-1] > n:
            money.pop()
        else:
            break

    dp = [1] + [0] * n
    for m in money:
        for i in range(m, n+1):
            dp[i] += dp[i-m]
    # print(dp)
    # print(n, money)
    return dp[n % 1000000007]
