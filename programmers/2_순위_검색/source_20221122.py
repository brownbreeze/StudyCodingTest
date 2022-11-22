conditions = list()

def check_info(arr, cnt):
    global conditions
    for i in range(len(conditions)):
        condition = conditions[i]
        if condition[0] != '-' and arr[0] != condition[0]:continue
        if condition[1] != '-' and arr[1] != condition[1]:continue
        if condition[2] != '-' and arr[2] != condition[2]:continue
        if condition[3] != '-' and arr[3] != condition[3]:continue
        if int(arr[4]) < int(condition[4]) :continue
        cnt[i] = cnt[i]+1
        
def solution(info, query):
    answer = []
    cnt = [0 for _ in query]
    global conditions
    conditions = list()
    for qur in query:
        arr = qur.split(" and ")
        arr.extend(arr.pop().split(" "))
        conditions.append(arr)
    
    for inf in info:
        arr = inf.split(" ")
        check_info(arr,cnt)
    return cnt
