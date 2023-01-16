def hanoi(arr, n, from_p, to_p, sub_p):
    if n == 1:
        arr.append([from_p, to_p])
      #  print(f'from_p({from_p})=> to_p({to_p})')
        return
    hanoi(arr, n-1, from_p, sub_p, to_p)
    arr.append([from_p, to_p])
   # print(f'from_p({from_p})=> to_p({to_p})')
    hanoi(arr, n-1, sub_p,to_p,from_p)
    
def solution(n):
    answer = []
    
    hanoi(answer, n, 1, 3, 2)
    return answer
