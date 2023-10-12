if __name__ == '__main__':
    score_list = []
    score_dict = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score not in score_list:
            score_list.append(score)
            score_dict[score] = [name]
        else: 
            score_dict[score].append(name)
    score_list.sort()
    score_dict[score_list[1]].sort() 
    for sc in score_dict[score_list[1]]:
        print(sc)    
    
