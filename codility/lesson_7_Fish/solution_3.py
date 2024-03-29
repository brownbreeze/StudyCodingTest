def solution(A: list, B: list) -> int:
    upstreamFish = []
    fishNumber = 0
    for i in range(len(A)):
        if B[i]: # fish is upstreaming
            upstreamFish.append(A[i])
            continue
        while True:
            if not upstreamFish:
                fishNumber += 1
                break
            if upstreamFish[-1] < A[i]:
                upstreamFish.pop()
                continue
            break
    fishNumber += len(upstreamFish)
    return fishNumber
 
