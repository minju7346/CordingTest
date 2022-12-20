key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

def rotate(arr):
    for i in range(len(arr)):
        tmp = arr[i][0]
        arr[i][0] = arr[i][1]
        arr[i][1] = len(arr)-1-tmp

key_one = []
lock_zero = []
for i, n in enumerate(key):
    for j, num in enumerate(n):
        if num == 1:
            key_one.append([i,j])
for i, n in enumerate(lock):
    for j, num in enumerate(n):
        if num == 0:
            lock_zero.append([i,j])
r_cnt = 0
while r_cnt < 4:
    for i in range(len(key_one)):
        p = key_one[i]
        key_one[i][0],key_one[i][1] = p[1], len(key)-1-p[0]
        #key_one[i] = (p[1], len(key)-1-p[0])
        print(key_one[i])

    r_cnt += 1
    for i in range(-(len(lock)-1), len(key)+len(lock)):
        for j in range(-(len(lock)-1), len(key)+len(lock)):
            z_cnt = len(lock_zero)
            for row, col in key_one:
                row += i
                col += j
                if (0<=row<len(lock)) and (0<=col<len(lock)):
                    if [row,col] in lock_zero:
                        z_cnt -= 1
                    else:
                        break
            if z_cnt == 0:
                print(True)
                exit(0)
print(False)
