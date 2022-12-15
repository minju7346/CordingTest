# 정렬된 리스트 기준으로 알파벳 차례대로 배정
# 매치된 것은 매치된 set에 넣어서 되었음을 알림
# 매치는 딕셔너리 이용해서 쉽게 가져 올 수 있도록 함
N = int(input())
arr = [input() for _ in range(N)]
num = 9
dict = {}
sum = 0
for i in arr:
    for idx, j in enumerate(i):
        if j in dict:
            dict[j] += 10 ** (len(i)-idx)
        else:
            dict[j] = 10 ** (len(i)-idx)
nlist = sorted(list(dict.items()),key=lambda x:x[1],reverse=True)
for i in nlist:
    dict[i[0]] = num
    num -= 1

for i in arr:
    tmp = ''
    for j in i:
        if j != '0':
            tmp += str(dict[j])
    sum += int(tmp)
print(sum)


