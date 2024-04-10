def solution(money):
    answer = 0
    l = len(money)
    dp1 = [0 for _ in range(l)]
    dp2 = [0 for _ in range(l)]

    dp1[0] = 0
    dp1[1] = money[1]
    for i in range(2, l):
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])

    dp2[0] = money[0]
    dp2[1] = max(money[1], money[0])
    for i in range(2, l-1):
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])

    return max(dp2[-2], dp1[-1])
