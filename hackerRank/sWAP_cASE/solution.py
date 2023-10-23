def swap_case(s):
    result = []
    for alpha in s:
        if ord(alpha) >= 97 and ord(alpha) <= 122:
            result.append(alpha.upper())
        else:
            result.append(alpha.lower())
            
    return ''.join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
