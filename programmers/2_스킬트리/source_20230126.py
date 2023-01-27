def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)
    # print(skill_list)
    for skill_tree in skill_trees:
        temp_skill = list(skill)
        for sk in skill_tree:
            if sk in temp_skill:
                if sk == temp_skill[0]:
                    temp_skill.pop(0)
                else:
                    break
        else:
            answer += 1
            # print(skill_tree)    
    return answer
