# 모든 문자열 붙이고, 숫자는 따로저장-> [0], [1]
# info 돌면서 in 되는것중에 점수가 더 놓은 것만 카운트
# 숫자로 먼저 continue로 걸러줌

def solution(info, query):
    result = [0]*len(query)
    info_table = ['']* len(info)
    query_table = [''] * len(query)
    for i, inf in enumerate(info):
        tmp = inf.split(' ')
        info_table[i] = tmp[:-1],tmp.pop()
    for i, que in enumerate(query):
        que = que.replace('and ', '')
        que = que.replace('- ', '')
        tmp = que.split(' ')
        query_table[i] = tmp[:-1],tmp.pop()
    for idx, q in enumerate(query_table):
        for i in info_table:
            if int(q[1]) <= int(i[1]):
                if set(q[0]) == (set(q[0]) & set(i[0])):
                    result[idx] += 1

    print(result)



print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))