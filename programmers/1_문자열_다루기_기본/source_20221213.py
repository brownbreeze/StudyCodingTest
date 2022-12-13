def solution(s):
    if len(s) not in [4,6]: return False
    if s.isnumeric(): return True
    return False
