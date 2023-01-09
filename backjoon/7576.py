from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([(i,j) for i in range(M) for j in range(N) if maps[i][j]==1])
if len(q) == 0:
    print(-1)
    exit(0)
visited = [[0]*N for _ in range(M)]
for x, y in q:
    visited[x][y] = 1
x, y = 0, 0
while q:
    x, y = q.popleft()
    for i in range(4):
        tx = x+dx[i]
        ty = y+dy[i]
        if 0<=tx<M and 0<=ty<N and not visited[tx][ty] and maps[tx][ty] == 0:
            visited[tx][ty] = 1
            maps[tx][ty] = maps[x][y] + 1
            q.append((tx, ty))
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0 and maps[i][j] != -1:
            print(-1)
            exit(0)

print(maps[x][y]-1)