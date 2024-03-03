import sys

arr = [1,1,1,2,2]
def check():
    for i in range(5,100):
        arr.append(arr[i-1]+arr[i-5])
    
def solution(num):
    return arr[num-1]
  
input = sys.stdin.readline
t = int(input())
q = []
for i in range(t):
    n = int(input())
    q.append(n) 
check()
for t in q:
    print(solution(t))