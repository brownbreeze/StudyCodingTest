g_dict={
    '[':1,
    ']':-1,
    '(':2,
    ')':-2,
    '{':3,
    '}':-3
}
def check_correct(li):
    global g_dict
    temp_li = list()
    for l in li:
        if not temp_li: 
            temp_li.append(g_dict[l])
            continue
        if g_dict[l] < 0:
            if len(temp_li) != 0 and temp_li[-1] == -1 * g_dict[l] :
                temp_li.pop()
            else: break
        else:
            temp_li.append(g_dict[l])
            
    if len(temp_li) !=0:
        del temp_li
        return False
    del temp_li
    return True

def solution(s):
    answer = -1
    s = list(s)
    result = list()
    for i in range(len(s)):
        result.append(check_correct(s))
        s.append(s.pop(0))
    return sum(result)
