import heapq

def solution(genres, plays):
    answer = []
    g_dic = {}
    m_dic = {}
    i = 0
    for gen in genres:
        g_dic[gen] = []
        m_dic[gen] = 0
    for gen, num in zip(genres, plays):
        heapq.heappush(g_dic[gen], (num,i))
        m_dic[gen] += num
        i += 1
    for key,value in g_dic.items():
        g_dic[key] = sorted(value)

    m_dic = sorted(m_dic.items(), key=lambda item: item[1], reverse=True)
    print(g_dic)
    for g in m_dic:
        t = []
        t1 = g_dic[g[0]].pop()
        if len(g_dic[g[0]]) == 0:
            answer.append(t1[1])
            continue
        t2 = g_dic[g[0]].pop()
        if t1[0] == t2[0] and t1[1] > t2[1]:
            answer.append(t2[1])
            answer.append(t1[1])
        else:
            answer.append(t1[1])
            answer.append(t2[1])
    return answer

print(solution(['a','b','c','d','a','d','d','d','a','a','c','c'],[100,300,400,150,100,300,200,600,700,110,900,9000]))
