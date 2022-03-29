from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#방향 벡터 - 상하좌우 순

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue :
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))

#가까운 노드부터 전 노드를 모두 순차적으로 탐색하기 떄문에 BFS가 적합하다



