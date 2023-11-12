def get_con(n, length):
    num = n
    for l in range(length-1):
        num *= 10
        num += n
    return num 

def add_data(n1, c1, n2, c2, nlist, clist):
    if n1 * n2 not in nlist :
        nlist.append(n1*n2)
        clist.append(c1+c2)
    if n2 != 0 and int(n1 / n2) not in nlist:
        nlist.append(int(n1/n2))
        clist.append(c1+c2)
    if n1 != 0 and int(n2 / n1) not in nlist:
        nlist.append(int(n2/n1))
        clist.append(c1+c2)
    if n1 + n2 not in nlist :
        nlist.append(n1+n2)
        clist.append(c1+c2)
    if n1 - n2 not in nlist:
        nlist.append(n1-n2)
        clist.append(c1+c2)
    if n2 - n1 not in nlist:
        nlist.append(n2-n1)
        clist.append(c1+c2)
    return nlist, clist
    
def solution(N, number):
    n_data = []
    c_data = []
    n_temp = []
    c_temp = []
    
    for i in range(7):
        n_temp = n_data.copy()
        c_temp = c_data.copy()
        
        n_temp.append(get_con(N, i+1))
        c_temp.append(i+1)

        for n1, c1 in zip(n_data, c_data) : 
            for n2, c2 in zip(n_data, c_data):
                if c1 + c2 > 8 : continue 
                n_temp,c_temp = add_data(n1, c1, n2, c2, n_temp, c_temp)
    
        if number in n_temp:
            return c_temp[n_temp.index(number)]
        
        n_data = n_temp.copy()
        c_data = c_temp.copy()
    
    return -1
