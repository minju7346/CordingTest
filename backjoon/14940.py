from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([(i,j) for i in range(n) for j in range(m) if maps[i][j]==2])
maps[q[0][0]][q[0][1]] = 0
visited = [[0]*m for _ in range(n)]
while q:
    x, y = q.popleft()
    for i in range(4):
        tx = x+dx[i]
        ty = y+dy[i]
        if 0<=tx<n and 0<=ty<m and maps[tx][ty] == 1 and not visited[tx][ty]:
            visited[tx][ty] = 1
            maps[tx][ty] = maps[x][y]+1
            q.append((tx, ty))
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and maps[i][j] == 1:
            maps[i][j] = -1
for i in range(n):
    for j in maps[i]:
        print(j, end=' ')
    print()
