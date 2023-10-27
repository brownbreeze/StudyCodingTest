def count_substring(string, sub_string):
    cnt = 0
    len_str = len(string)
    len_sub = len(sub_string)
    for i in range(0, len_str-len_sub+1):
        # print(sub_string, string[i:][:len_sub])
        if sub_string in string[i:][:len_sub]:
            cnt += 1
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

