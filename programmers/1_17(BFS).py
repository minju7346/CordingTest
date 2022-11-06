# 최단거리 중 배열 문제는 BFS이용(큐 사용)
# 방향 변수는 다르면 방향을 바꿧음을 의미
# -> 같은 방향은 나올수가 없기때문(위로갓다 아래로?x) 즉 바뀌면 무조건 턴 한 것

import sys
from collections import deque

def solution(board):
    def bfs(start):
        dic = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]} # 방향좌표 생성
        b_len = len(board)
        visited = [[sys.maxsize] * b_len for _ in range(b_len)] # 각 좌표 값 금액 최대로 설정(방문시 무조건 바뀌게 하기위해서)
        visited[0][0] = 0 # 시작 값 0으로 초기화

        q = deque([start])
        while q: # 모든 방향으로 돌면서 결국 가장 작은 값들로 배열들을 저장함
            x,y,c,d = q.popleft()
            for i in range(4):
                nx = x + dic[i][0]
                ny = y + dic[i][1]

                if 0<=nx<b_len and 0<=ny<b_len and board[nx][ny] == 0: # 범위안에 들어오고, 막혀있지 않다면
                    nc = c+100 if i == d else c+600 #직선이면 +100, 코너면 +600
                    if nc < visited[nx][ny]: # 방문했음을 나타냄
                        visited[nx][ny] = nc
                        q.append([nx, ny, nc, i]) # 업뎃됬다면 큐에 넣어놈

        return visited[-1][-1] # 맨 마지막 배열 값 리턴

    return min([bfs((0,0,0,1)), bfs((0,0,0,2))]) # 처음에 동남쪽으로만 출발 가능하기때문에 두 함수만 호출

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))