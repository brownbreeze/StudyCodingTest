def get_two_char(str):
    if len(str) < 2: return [str]
    li = []
    for i in range(len(str)-1):
        if str[i].isalpha() is False or str[i+1].isalpha() is False: continue
        li.append(str[i:i+2])
    return len(li), li
        
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) == 0 and len(str2) == 0 : return 65536

    cnt_li1, st1_li = get_two_char(str1)
    cnt_li2, st2_li = get_two_char(str2)
    if len(st1_li) == 0 and len(st2_li) == 0 : return 65536

    gp_cnt = 0 
    for st1_l in st1_li:
        if st1_l in st2_li:
            st2_li.pop(st2_li.index(st1_l))
            gp_cnt = gp_cnt + 1 
    return int(gp_cnt/(cnt_li1+cnt_li2-gp_cnt)*65536)
