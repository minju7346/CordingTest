from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, k = map(int, input().split())
graph = [[] * (n+1) for i in range(n+1)]
gmap = [[] * (n+1) for i in range(n+1)]
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    gmap[i] = arr
    for j, m in zip(arr, range(1, n+1)):
        if j != 0:
            graph[j].append((i,m))
s, x, y = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
for _ in range(s):
    for i in range(1, k+1):
        while graph[i]:
            queue.append(graph[i].pop())
        while queue :
            x, y = queue.popleft()
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if nx <= 0 or ny <= 0 or nx > n or ny > n:
                    continue
                if gmap[nx][ny-1] == 0:
                    gmap[nx][ny-1] = i
                    queue.append((nx,ny))
            print(gmap)

