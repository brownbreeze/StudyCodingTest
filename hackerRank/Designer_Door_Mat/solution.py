if __name__ == '__main__':
    y, x = input().split(' ')
    y = int(y)
    x = int(x)
    
    mid_line = y//2 
    start_point = [int(x//2-1), int(x//2+2)]
    for ty in range(y): 
        if ty == mid_line:
            for tx in range(int((x-7)/2)):
                print('-', end="")
            print('WELCOME', end="")
            for tx in range(int((x-7)/2)):
                print('-', end="")
        else : 
            for tx in range(x):
                if tx < start_point[0] or tx >= start_point[1]:
                    print('-', end="")
                elif (tx)%3 == 1: 
                    print('|', end="")
                else:
                    print('.', end="")
        print()
        if ty < mid_line-1: 
            start_point[0] -=3
            start_point[1] +=3
        elif ty > mid_line: 
            start_point[0] +=3
            start_point[1] -=3
        
