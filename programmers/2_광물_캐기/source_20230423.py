from collections import deque
piro_table = [[1,1,1],[5,1,1],[25,5,1]]
def get_piro(gock, cur_piro, min_list):
    for i in range(3):
        cur_piro += piro_table[gock][i] *min_list[i]
    return cur_piro 

def solution(picks, minerals):
    answer = -1
    # dia, iron, stone
    mnl_len = len(minerals)
    queue = deque([[0, picks, 0]])

    while True:
        if len(queue) == 0 : break
        idx, cur_pick, cur_piro = queue.popleft()
        if idx == mnl_len or cur_pick.count(0) == 3:
            answer = cur_piro if answer == -1 or cur_piro < answer else answer
            continue
        
        idx_fiv = mnl_len if idx+5 > mnl_len else idx+5
        mns_cnt = [ 
            minerals[idx:idx_fiv].count("diamond"),
            minerals[idx:idx_fiv].count("iron"),
            minerals[idx:idx_fiv].count("stone")
            ]
        for i in range(3):
            if cur_pick[i] == 0: continue
            cur_pick[i] -= 1
            queue.append([idx_fiv, cur_pick.copy(), get_piro(i, cur_piro, mns_cnt)])
            cur_pick[i] += 1
    return answer
