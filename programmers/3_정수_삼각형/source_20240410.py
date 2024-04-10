def solution(triangle):
    answer = 0
    ts = len(triangle)
    dp = [[0 for _ in range(ts)] for _ in range(ts)]
    dp[0][0] = triangle[0][0]

    l = 0
    for row in triangle:
        l += 1
        for i in range(len(row)):
            if i == 0:
                dp[l-1][i] = dp[l-2][i] + row[i]
            elif i == l-1:
                dp[l-1][i] = dp[l-2][i-1] + row[i]
            else:
                dp[l-1][i] = max(dp[l-2][i-1] + row[i], dp[l-2][i] + row[i])
    return max(dp[-1])
