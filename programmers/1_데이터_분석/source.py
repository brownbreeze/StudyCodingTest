def solution(data, ext, val_ext, sort_by):
    pos = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    data = [d  for d in data if d[pos[ext]] <= val_ext]
    data.sort(key=lambda x: x[pos[sort_by]], reverse=False)
    return data
