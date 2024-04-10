def solution(s):
    answer = 1
    l = len(s)
    dp = [[0 for _ in range(l)] for _ in range(l)]

    for i in range(l):
        dp[i][i] = 1

    for i in range(l-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 1
            answer = 2

    for k in range(3, l+1):
        for i in range(l-k+1):
            j = i+k-1
            if s[i] == s[j] and dp[i+1][j-1] == 1:
                dp[i][j] = 1
                answer = max(answer, k)

    # print(dp)
    return answer
