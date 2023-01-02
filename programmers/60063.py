from collections import deque

def can_move(cur1, cur2, new_board):
    X, Y = 0, 1
    cand = []
    #평행이동
    DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dx, dy in DELTAS:
        nxt1 = (cur1[X] + dx, cur1[Y] + dy)
        nxt2 = (cur2[X] + dx, cur2[Y] + dy)
        if new_board[nxt1[X]][nxt1[Y]] == 0 and new_board[nxt2[X]][nxt2[Y]] == 0:
            cand.append((nxt1, nxt2))
    #회전-가로방향일때(최대 4개)
    if cur1[X] == cur2[X]:
        UP, DOWN = -1, 1
        for d in [UP, DOWN]:
            if new_board[cur1[X]+d][cur1[Y]] == 0 and new_board[cur2[X]+d][cur2[Y]] == 0:
                cand.append((cur1, (cur1[X]+d, cur1[Y])))
                cand.append((cur2, (cur2[X]+d, cur2[Y])))
    #회전-세로방향일때
    else:
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if new_board[cur1[X]][cur1[Y]+d] == 0 and new_board[cur2[X]][cur2[Y]+d] == 0:
                cand.append(((cur1[X]+d, cur1[Y]), cur1))
                cand.append(((cur2[X] + d, cur2[Y]), cur2))
    return cand


def solution(board):
    N = len(board)
    new_board = [[1]*(N+2) for _ in range(N+2)] #못빠져나가게 가두리역할
    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]

    q = deque([((1, 1), (1, 2), 0)]) # deque에 넣을때는 항상 패킹해서 넣음-append등 전달인자가 하나여야 해서
    visited = set([((1, 1), (1, 2), 0)])

    while q:
        cur1, cur2, cnt = q.popleft()
        if cur1 == (N, N) or cur2 == (N, N):
            return cnt
        for nxt in can_move(cur1, cur2, new_board):
            if nxt not in visited:
                q.append((*nxt, cnt+1)) #nxt를 언패킹해서 세개를 패킹하여 전달
                visited.add(nxt)
print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))