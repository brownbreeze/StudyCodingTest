if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    arr = []
    for tx in range(x+1):
        for ty in range(y+1):
            for tz in range(z+1):
                if tx+ty+tz != n: 
                    arr.append([tx,ty,tz])
    print(arr)        
