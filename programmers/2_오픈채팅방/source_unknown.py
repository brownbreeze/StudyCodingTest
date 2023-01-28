def solution(record):
    answer = []
    names = dict()
    inout = []
    for his in record : 
        his_li = his.split(' ')
        # print(his_li)
        cmd = his_li[0]
        uid = his_li[1]
        if cmd != 'Leave':
            name = his_li[2]    
            names[str(uid)] = name
        #inout.append({cmd,uid})
    
    print(names)
    return answer
