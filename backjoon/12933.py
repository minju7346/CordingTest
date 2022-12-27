ducks = [[' '] for _ in range(10)]
cnt = 0
q = 'quack'
s = input()
now,index = 0, -1

for i in s:
    if i == 'q':
        now += 1
        index += 1
        ducks[index] = i
        cnt = max(cnt, now)
    else:
        flag = 0
        if i == 'k':
            now -= 1
        for idx in range(index+1):
            if ducks[idx] == q[q.index(i)-1]:
                flag = 1
                ducks[idx] = i
                break
        if flag == 0:
            print(-1)
            exit(0)
for i in range(index+1):
    if ducks[i] != 'k':
        print(-1)
        exit(0)
print(cnt)
