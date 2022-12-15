T = int(input())
while T != 0:
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()
    cut = arr[0][1]
    for i, j in arr:
        if j > cut:
            N -= 1
        else:
            cut = j
    print(N)
    T -= 1
