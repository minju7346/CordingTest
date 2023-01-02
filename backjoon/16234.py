from collections import deque

N, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append([x,y]) # 큐는 항상 나중에 append로 추가해 줄것
    temp = [[x, y]]
    while q:
        a, b = q.popleft()
        for k in range(4): #bfs의 경우 상하좌우 움직임일떄 pop후 바로 4방향 for문돌림
            tx = a + dx[k]
            ty = b + dy[k]
            if 0 <= tx < N and 0 <= ty < N and visited[tx][ty] == 0:#범위에 들어오나+방문했나
                if L <= abs(maps[a][b] - maps[tx][ty]) <= R:# 문제별 조건확인
                    visited[tx][ty] = 1 #해당시 방문 및 큐 추가
                    q.append([tx, ty])
                    temp.append([tx, ty])
    return temp

cnt = 0
while True:
    flag = 1
    visited = [[0] * N for _ in range(N)] # bfs는 방문기록함수 필요할 수 있음
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                tmp = bfs(i, j)
                if len(tmp) > 1:
                    flag = 0
                    num = sum([maps[x][y] for x, y in tmp]) // len(tmp)
                    for x, y in tmp:
                        maps[x][y] = num
    if flag:
        break
    cnt += 1

print(cnt)
