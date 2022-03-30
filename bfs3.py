from collections import deque
n, k = map(int, input().split())
graph = [[] * (k+1) for _ in range(k+1)]
gmap = [[] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    gmap[i] = arr
    for j, m in zip(arr, range(1, n+1)):
        if j != 0:
            graph[j].append((i, m))
s, a, b = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph.sort()
for k in range(s):
    print(k)
    for i in range(1, k+1):
        queue = deque()
        while graph[i]:
            queue.append(graph[i].pop())
            x, y = queue.popleft()
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if nx <= 0 or ny <= 0 or nx > n or ny > n:
                    continue
                if gmap[nx][ny-1] == 0:
                    gmap[nx][ny-1] = i
                    queue.append((nx, ny))
        graph[i] = queue

print(gmap[a][b-1])
