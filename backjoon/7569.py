from collections import deque

N, M, H = map(int, input().split())
maps = []
for i in range(H):
    maps.append([list(map(int, input().split())) for _ in range(M)])

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque([(z, i, j) for i in range(M) for j in range(N) for z in range(H) if maps[z][i][j]==1])

if len(q) == 0:
    print(-1)
    exit(0)

visited = [[[0]*N for _ in range(M)] for _ in range(H)]

for z, x, y in q:
    visited[z][x][y] = 1
z, x, y = 0, 0, 0
while q:
    z, x, y = q.popleft()
    for i in range(6):
        tz = z+dz[i]
        tx = x+dx[i]
        ty = y+dy[i]
        if 0<=tx<M and 0<=ty<N and 0<=tz<H and not visited[tz][tx][ty] and maps[tz][tx][ty] == 0:
            visited[tz][tx][ty] = 1
            maps[tz][tx][ty] = maps[z][x][y] + 1
            q.append((tz, tx, ty))
for k in range(H):
    for i in range(M):
        for j in range(N):
            if visited[k][i][j] == 0 and maps[k][i][j] != -1:
                print(-1)
                exit(0)
big = 0
for z in range(H):
    for i in range(M):
        big = max(max(maps[z][i]), big)
print(big-1)