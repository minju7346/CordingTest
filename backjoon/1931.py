#최대한 많이 해야함->끝내는 순서가 빠른것==다음 회의들을 시작할 시간이 더 많은것
num = int(input())
arr = [list(map(int,input().split())) for _ in range(num)]
arr.sort(key = lambda x : (x[1],x[0]))

end, sum = 0, 0
for i in arr:
    if i[0] >= end:
        end = i[1]
        sum += 1
print(sum)
