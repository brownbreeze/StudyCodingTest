def solution(genres, plays):
    answer = []
    temp = []
    len_song = len(genres)
    genres_dict = dict()
    for i in range(len_song):
        if genres[i] in genres_dict:
            genres_dict[genres[i]][0] += plays[i]
            genres_dict[genres[i]][1].append([i, plays[i]])
        else:
            genres_dict[genres[i]] = [plays[i], [[i, plays[i]]]]
    
    for gen_name in genres_dict:
        genres_dict[gen_name][1].sort(key = lambda item : item[1], reverse=True)
    sorted_dict = sorted(genres_dict.items(), key = lambda item: item[1][0], reverse = True)
    max_len = min(2, len(genres_dict))
    for i in range(len(genres_dict)):
        k, value = sorted_dict[i]
        value_list = value[1]
        for j in range(2):
            if len(value[1]) <= j: break
            answer.append( value_list[j][0] )            
    return answer
