if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort(reverse=True)
    maxn = arr[0]
    for a in arr: 
        if a != maxn : 
            print(a)
            break
            
