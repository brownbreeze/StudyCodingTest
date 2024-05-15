def solution(sticker):
    answer = 0
    stlen = len(sticker)
    arr = [0 for _ in range(stlen)]
    first = 0
    if stlen == 2:
        return max(sticker)
    if stlen == 1:
        return sticker[0]

    arr[0] = sticker[0]
    arr[1] = max(sticker[0], sticker[1])
    for i in range(2, stlen-1):
        n1 = arr[i-2]+sticker[i]
        if n1 > arr[i-1]:
            arr[i] = n1
        else:
            arr[i] = arr[i-1]
    first = arr[-2]   
    arr[0] = 0
    arr[1] = sticker[1]
    for i in range(2, stlen):
        n1 = arr[i-2]+sticker[i]
        if n1 > arr[i-1]:
            arr[i] = n1
        else:
            arr[i] = arr[i-1]
    return max(first, arr[-1])
