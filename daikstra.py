import heapq


def solution(n, costs):
    distances = [1e9] * (n+1)
    graph = [[] for i in range(n+1)]
    for i in range(n):
        a = costs[i][0]
        b = costs[i][1]
        c = costs[i][2]
        graph[a].append((b, c))  # start로 부터의 거리 값을 저장하기 위함
    distances[0] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [distances[0], 0])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        # 탐색 할 노드, 거리를 가져옴.
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue

        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = distance
                # 다음 인접 거리를 계산 하기 위해 큐에 삽입
                heapq.heappush(queue, [distance, new_destination])

    return distances


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
