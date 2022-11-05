# 다익스트라 알고리즘 이용 -> 함수 활용하여 풀기
# -> 해당 함수는 건드리지 말고 최단 경로를 찾아주는 하나의 메서드로 볼 것
# 문제에 맞게 메인함수만 바꿔주면 됨
from heapq import heappop, heappush

INF = int(1e9)

def dijkstra(src, dst):
    global graph
    table = [INF for i in range(len(graph))]
    table[src] = 0
    pq = [[0, src]]

    while pq: #큐에 남은것이 없을때 까지 회전
        w, x = heappop(pq) # 우선순위가 높은(현재 src노드에서 가장 거리가 짧은 노드 pop

        if table[x] < w: continue # 이미 최솟값으로 갱신된 경우 무시함

        for item in graph[x]:
            nx, ncost = item[0], item[1]
            ncost += w
            if ncost < table[nx]:
                table[nx] = ncost
                heappush(pq, [ncost, nx])
    return table[dst]



def solution(n, s, a, b, fares):
     # 행이 n+1개인 배열을 만들어줌
    global graph
    graph = [[] for i in range(n + 1)]
    cost = INF

    for x, y, c in fares:  # 인접행렬로 저장
        graph[x].append([y, c])
        graph[y].append([x, c])

    for i in range(1, n + 1):
        cost = min(cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
    return cost


print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))