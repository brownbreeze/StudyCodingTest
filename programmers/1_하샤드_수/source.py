def solution(x):
    sm = 0
    tx = x
    while True:
        if x <10:
            sm += x
            break
        sm += x%10
        x = x//10
    # print(x,sm)
    if tx%sm == 0:
        return True
    return False

