bingo = [list(map(int,input().split())) for _ in range(5)]
innum = []
arr = [[0]*5 for _ in range(5)]

def bingo_yes(arr):
    cnt = 0
    for a in range(5):
        if sum(arr[a]) == 5:
            cnt += 1
    for j in range(5):
        tot = 0
        for a in range(5):
            tot += arr[a][j]
        if tot == 5:
            cnt += 1
    if arr[0][0]+arr[1][1]+arr[2][2]+arr[3][3]+arr[4][4] == 5:
        cnt += 1
    if arr[4][0]+arr[3][1]+arr[2][2]+arr[1][3]+arr[0][4] == 5:
        cnt += 1
    if cnt >= 3:
        return True
    else:
        #print(arr,cnt)
        return False

for i in range(5):
    innum += list(map(int,input().split()))
for idx, i in enumerate(innum):
    for row in range(5):
        if i in bingo[row]:
            col = bingo[row].index(i)
            arr[row][col] = 1
    if bingo_yes(arr):
        print(idx+1)
        break
