def solution(a, b):
    result_list = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    mon_day = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = sum(mon_day[:a-1])
    days+=(b+4)
    days%=7
    return result_list[days]
