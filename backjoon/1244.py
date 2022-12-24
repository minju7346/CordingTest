N = int(input())
switch = list(map(int, input().split()))
num = int(input())
stu = [list(map(int,input().split())) for _ in range(num)]

for s, a in stu:
    if s == 1: # 남학생
        cnt = N//a
        for i in range(cnt):
            if switch[a*(i+1)-1] == 0:
                switch[a*(i+1)-1] = 1
            else:
                switch[a*(i+1)-1] = 0
    else:
        if switch[a-1] == 1:
            switch[a-1] = 0
        else:
            switch[a-1] = 1
        idx = 1
        l, r = a - idx-1, a + idx-1
        while 0<=l<N and 0<=r<N:
            if switch[l] == switch[r]:
                if switch[l] == 1:
                    switch[l] = 0
                else:
                    switch[l] = 1
                if switch[r] == 1:
                    switch[r] = 0
                else:
                    switch[r] = 1
            else:
                break
            idx += 1
            l, r = a - idx-1, a + idx-1
for idx, i in enumerate(switch):
    print(i,end = ' ')
    if (idx+1)%20 == 0:
        print()


