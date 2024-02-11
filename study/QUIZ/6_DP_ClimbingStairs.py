# def cs(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return cs(n-1) + cs(n-2)

memo = {}
def cs(n):
    # bottom up
    if n == 1:
        return 1
    if n == 2:
        return 2
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[i]
    