# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter 

if __name__ == '__main__':
    answer = 0 
    total = input()
    value_list = input().split(' ')
    vc = Counter(value_list)
    # print(vc)
    cnt = input()
    for i in range(int(cnt)):
        size, value = input().split(' ')
        size = str(size)
        value = int(value)
        # print(size, value , vc)
        if size in vc.keys() and vc[size] > 0:
            vc[size] -=1
            answer += value
            # print(answer, value)
    print(answer)
