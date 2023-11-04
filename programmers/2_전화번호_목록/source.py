def solution(phone_book):
    answer = True
    len_book = len(phone_book)
    phone_book.sort()
    for i in range(0,len_book-1):
        j = i+1
        max_len = min(len(phone_book[i]), len(phone_book[j]))
        if phone_book[i][:max_len] == phone_book[j][:max_len]:
            return False
    return True
