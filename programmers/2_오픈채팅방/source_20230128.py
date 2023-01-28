def solution(record):
    answer = []
    user_data = dict()
    history_data = []
    for rcd in record:
        datas = rcd.split(' ')
        if datas[0] == 'Enter':
            user_data[datas[1]]=datas[2]
            history_data.append([datas[1],0])# 0 in, 1 out
        elif datas[0] == 'Leave':
            history_data.append([datas[1],1])# 0 in, 1 out
        else: # change
            user_data[datas[1]]=datas[2]
    for history in history_data:
        if history[1]==0: # in
            answer.append(f'{user_data[history[0]]}님이 들어왔습니다.')
        else: # out
            answer.append(f'{user_data[history[0]]}님이 나갔습니다.')
    return answer
