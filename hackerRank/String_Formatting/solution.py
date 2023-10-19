def print_formatted(number):
    lenn = len(format(number, 'x'))
    
    for num in range(1, number+1):
        b = str(format(num, 'b'))
        o = str(format(num, 'o'))
        h = str(format(num, 'x'))
        print(str(num).rjust(lenn), end=" ")
        print(o.rjust(lenn), end=" ")
        print(h.rjust(lenn), end=" ")
        print(b.rjust(lenn))
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
