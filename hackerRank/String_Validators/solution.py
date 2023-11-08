if __name__ == '__main__':
    s = input()
    for a in s:
        if a.isalnum():
            print("True")
            break
    else:
        print("False")
    for a in s:
        if a.isalpha():
            print("True")
            break
    else:
        print("False")
    for a in s:
        if a.isdigit():
            print("True")
            break
    else:
        print("False")
    for a in s:
        if a.islower():
            print("True")
            break
    else:
        print("False")
    for a in s:
        if a.isupper():
            print("True")
            break
    else:
        print("False")
    
