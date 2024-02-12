# bottom up
cost = [10, 15, 20, 17, 1]
def dp(n):
    memo = [-1]*n
    memo[0] = 0
    memo[1] = 0
    for i in range(2, n+1):
        memo[n] = min(dp(n-1) + cost[n-1], dp(n-2) + cost[n-2])
    return memo[n]