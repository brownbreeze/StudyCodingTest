def go_func(s):
    new_s = list(s)
    c = new_s.count('1')
    return new_s.count('0'), "{0:b}".format(c)
    
def solution(s):
    answer = [0,0]
    while True:
        del_num, new_s = go_func(s)
        answer[1] += del_num
        answer[0] += 1
        # print(new_s, del_num)
        s = new_s
        if s == '1':break
    return answer
