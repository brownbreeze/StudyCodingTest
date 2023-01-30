def solution(files):
    answer = []
    NUMBER_LIST = ['0','1','2','3','4','5','6','7','8','9']
    for file in files:
        number_flag = 0
        tail_flag = 0
        for i in range(len(file)):
            alpha = file[i]
            if number_flag == 0 and alpha in NUMBER_LIST:
                number_flag = i
            elif number_flag != 0  and (alpha not in NUMBER_LIST or i-number_flag>=5):
                tail_flag = i
                break
        else:
            tail_flag = len(file)
        answer.append({'file':file,
                      'head':file[:number_flag].lower(),
                      'number':int(file[number_flag:tail_flag]),
                      'tail':file[tail_flag:]})
    # print(answer)
    answer = sorted(answer, key=lambda x:(x['head'],x['number']))
    return [data['file'] for data in answer]
