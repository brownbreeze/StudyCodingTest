def print_rangoli(size):
    # your code goes here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    print_rows = []
    for r in range(size):
        print_arr = []
        for i in range((size-r-1)*2):
            print_arr.append('-')
        for i in range(r+1):
            print_arr.append(alphabet[size-i-1])
            print_arr.append('-')
        print_arr.pop()
        copy_arr = print_arr.copy() 
        copy_arr.pop()
        print_arr += copy_arr[::-1]
        
        print(''.join(print_arr))
        print_rows.append(''.join(print_arr))
    print_rows.pop()
    for i in range(1, size):
        print(print_rows.pop())
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
