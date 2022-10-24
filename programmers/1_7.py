#1,4,7은 L, 3,6,9는 R을 Answer에 추가
#2,5,8,0-> 1. 누가 더 가깝나 2. 같다면 무슨손 잡이인지
#움직일때마다 각 손의 위치 저장
#거리 정하는 함수 생성
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
answer = ""
p_dict = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1),
          6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), '*':(3,0), 0:(3,1), '#':(3,2)}
l_pos = '*'
r_pos = '#'
for i in numbers:
    if i in (1,4,7):
        answer += "L"
        l_pos = i
    elif i in (3,6,9):
        answer += "R"
        r_pos = i
    else:
        l_dis = abs(p_dict[l_pos][0]-p_dict[i][0])+abs(p_dict[l_pos][1]-p_dict[i][1])
        r_dis = abs(p_dict[r_pos][0]-p_dict[i][0])+abs(p_dict[r_pos][1]-p_dict[i][1])
        if l_dis < r_dis:
            answer += "L"
            l_pos = i
        elif l_dis > r_dis:
            answer += "R"
            r_pos = i
        else:
            if hand == "right":
                answer += "R"
                r_pos = i
            else:
                answer += "L"
                l_pos = i
print(answer)