#무작위로 1을 세개 추가하고 2주변 0개수세는 bfs로 돌리면서 모든 결과의 최솟값 구함
from itertools import combinations
from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(t):
    q = deque(twos)
    tot = 0
    visited = [[0]*M for _ in range(N+1)]
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        if t[x][y] == 2 or t[x][y] == 0:
            t[x][y] = 3
            tot += 1
            for i in range(4):
                tx = x+dx[i]
                ty = y+dy[i]
                if 0<=tx<N and 0<=ty<M and not visited[tx][ty]:
                    q.append((tx,ty))
    for i in range(N):
        tot += t[i].count(1)
    return N*M - tot
N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
zeros, twos = [], []
result = 0
for i, m in enumerate(map):
    for j, num in enumerate(m):
        if num == 0:
            zeros.append([i,j])
        elif num == 2:
            twos.append([i,j])
for z1, z2, z3 in combinations(zeros,3):
    tmp = copy.deepcopy(map)
    tmp[z1[0]][z1[1]] = 1
    tmp[z2[0]][z2[1]] = 1
    tmp[z3[0]][z3[1]] = 1
    result = max(bfs(tmp), result)
print(result)





