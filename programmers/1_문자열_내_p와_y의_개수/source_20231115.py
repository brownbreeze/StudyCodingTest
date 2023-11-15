def solution(s):
    return (len([c for c in s if c =='Y' or c =='y'])==len([c for c in s if c =='P' or c =='p']))
