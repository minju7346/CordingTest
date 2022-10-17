#4*n 배열을 만들어서 업데이트 형식으로
#In을 Out로 바꿀때마다 가격값 업데이트해주고 마지막에 Out만 찾아서 11:59분으로 계산하여 업데이트
#람다 함수로 자동차 번호기준을 이용해 정렬 후 출력
#업데이트를 해야하는지(기존에 들어온적이 있는지) 아는 방법은??
#딕셔너리를 키는 자동차 넘버 밸류는 (IN/OUT, 현재시간, 누적금액)
#1. 딕셔너리에 있는 넘버인가?
#1-1, 1-2. In/Out중 무엇인가 - record값이 Out일경우 누적금액 업뎃 / In일 경우 현재시간 업뎃
#2. 딕셔너리에 없는가? -> 딕셔너리에 추가
import math
#3. 마지막에 딕셔너리 값들중에서(items..?)돌면서 In인 것들 값 업뎃 및 OUT값 정산하여 리스트에 추가
#4. 키값으로 정렬 후 누적금액으로 새로운 result만들어서 리턴.
# 누적된 시간에 새로 더해줌
fee = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
car = {}
result = []
for i in records:
    print(car)
    tmp_time, num, stat = i.split(" ")
    time = int(tmp_time[0:2])*60 + int(tmp_time[3:])
    if num not in car: #처음 나온 차량번호
        car[num] = [stat, time]
    elif stat == "IN": #이미 등록된 차량에 업데이트
        tmp = car[num]
        car[num] = ["IN", time-tmp[1]]
    else:
        tmp = car[num]
        car[num] = ["OUT", time-tmp[1]]

for k, v in sorted(car.items()):
    print(v)
    if v[0] == "IN":
        v[1] = 1439 - v[1]
    if v[1] > fee[0]:  # 기본시간 넘었을 경우
        result.append(fee[1] + math.ceil((v[1] - fee[0]) / fee[2]) * fee[3])
    else:
        result.append(fee[1])
