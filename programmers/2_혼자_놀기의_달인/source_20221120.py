def solution(cards):
    answer = 0
    opened = [ False for _ in cards]    
  
    for i in range(len(cards)):
        idx = i
        opened = [ False for _ in cards]
        opened[idx] = True
        idx = cards[idx]
        while True:
            if opened[idx-1] : break
            opened[idx-1] = True
            idx = cards[idx-1]
        if sum(opened) == len(cards) : continue
        cnt = sum(opened)
        for j in range(len(cards)):
            if opened[j] : continue
            idx = j 
            opened_scd = opened[:]
            opened_scd[idx] = True
            idx = cards[idx]
            while True:
                opened_scd[idx - 1] = True
                if opened_scd[cards[idx-1]-1]: break
                idx = cards[idx-1]
            answer = max(answer , cnt * (sum(opened_scd)-cnt))
    return answer
