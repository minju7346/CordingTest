def solution(participant, completion):
    p_dic = {}
    answer = ''
    for i in participant:
        if i in p_dic.keys():
            p_dic[i] += 1
        else:
            p_dic[i] = 1
    for i in completion:
        p_dic[i] -= 1
    for key,value in p_dic.items():
        if value == 1:
            answer = key
    return answer