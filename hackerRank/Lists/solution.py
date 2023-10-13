if __name__ == '__main__':
    N = int(input())
    arr = []
    for n in range(N):
        input_str = input().split(' ')        
        
        cmd = input_str[0]
        if cmd == 'insert':
            arr.insert(int(input_str[1]), int(input_str[2]))
        elif cmd == 'print':
            print(arr)
        elif cmd == 'remove':
            arr.remove(int(input_str[1]))
        elif cmd == 'append':
            arr.append(int(input_str[1]))
        elif cmd == 'sort':
            arr.sort()
        elif cmd == 'pop':
            arr.pop()
        elif cmd == 'reverse':
            arr.reverse()

