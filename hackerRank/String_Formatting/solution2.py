def print_formatted(number):
    lenn = len(str(format(number, 'b')))

    for num in range(1, number+1):
        n = str(num).rjust(lenn)
        b = str(format(num, 'b')).rjust(lenn)
        o = str(format(num, 'o')).rjust(lenn)
        h = str(format(num, 'X')).rjust(lenn)
        print(n, o, h, b)
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
