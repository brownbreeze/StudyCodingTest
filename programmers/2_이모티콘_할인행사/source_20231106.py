def value(num, pos, users, emoticons):
    el = len(emoticons)
    val = list()
    for i in range(el):
        val.append(int(num%4))
        num = num / 4
    
    tickets = 0
    real_value = 0
    
    for percen, value in users:
        total_value = 0
        for i in range(el):
            if (val[i]+1)*10 >= percen:
                total_value+=emoticons[i]* (9-val[i])*10/100.0
        if total_value >= value:
            tickets +=1
        else:
            real_value += total_value
    #     print('  > ', total_value)
    # print(val, tickets, real_value)    
    # print()
    return [tickets, real_value]
    
def solution(users, emoticons):
    # answer = []
    total = 4**len(emoticons)
    
    i = 0 
    max_t = 0
    max_v = 0
    while i<total:
        num = i
        t, v = value(num, 0, users, emoticons)
        if max_t < t:
            max_t = t
            max_v = v
        elif max_t == t:
            max_v = max(max_v, v)
        
        i+=1         
    return [max_t, max_v]

