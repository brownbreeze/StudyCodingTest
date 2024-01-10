def get_days(day):
    today_datas = day.split('.')
    return int(today_datas[0])*28*12 + int(today_datas[1])*28 + int(today_datas[2])
    
    
def solution(today, terms, privacies):
    answer = []
    today_cnt = get_days(today)
    
    term_dict = dict()
    for term in terms:
        t = term.split()
        term_dict[t[0]] = int(t[1]) * 28

    i = 0
    for privacy in privacies:
        i+=1
        temp = privacy.split()
        if today_cnt >= get_days(temp[0]) + term_dict[temp[1]]:
            answer.append(i)
    
    return answer
