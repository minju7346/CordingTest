# 만약x라면 먼저주어진 배열을 통해 주변에 몇개의 지뢰가있는지 반환하는 함수에 넣고
# 해당값을 바꿔줌

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def num_bumbs(x, y):
    cnt = 0
    for b in range(8):
        tx = x + dx[b]
        ty = y + dy[b]
        if 0 <= tx < N and 0 <= ty < N:
            if bumb[tx][ty] == '*':
                cnt += 1
    arr[x][y] = str(cnt)


def star():
    for ii in range(N):
        for jj in range(N):
            if bumb[ii][jj] == '*':
                arr[ii][jj] = '*'

N = int(input())
bumb = [list(input()) for _ in range(N)]
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'x':
            if bumb[i][j] == '*':
                star()
            else:
                num_bumbs(i, j)
for i in range(N):
    print(''.join(arr[i]))
