def find_dungeons(pee, dgs, gone, cnt):
    result = []
    visited = False
    if pee <= 0 : return cnt
    for i  in range(len(dgs)):
        g = gone[i]
        dg = dgs[i]

        if g == 1 : continue
        if pee < dg[0]: continue
        gone[i] = 1
        visited = True
        #print(f'{i} 바ㅇ문, {gone}, pee={pee}, cnt={cnt}')
        result.append(find_dungeons(pee - dg[1], dgs, gone, cnt+1))
        gone[i] = 0
    if visited == False:
        return cnt
    return max(result)

def solution(k, dungeons):
    answer = -1
    gone = [0 for _ in dungeons]
    answer = find_dungeons(k, dungeons, gone, 0)
    return answer
