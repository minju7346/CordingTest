#1. Enter일때 - 아이디/닉네임를 사전에 저장,반환리스트에 "아이디 님이 들어옴"로 저장
#2. Leave일때 - "아이디 님이 나갔음"을 저장
#3. Change일때 - 해당 키를 찾아서 이름을 바꿔줌
# "아이디 들어옴/나감"을 반환할 리스트에 저장 후 마지막에 포문 돌면서 안에 내용을 바꿈
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
result = []
n_dict = {}

for i in record:
    if i[0] == "L":
        result.append(i.split(' ')[1]+'*'+"님이 나갔습니다.")
        continue
    a, id, name = i.split(' ')
    if a == "Enter":
        n_dict[id] = name
        result.append(id+'*'+"님이 들어왔습니다.")
    else:
        n_dict[id] = name
r_len = len(result)
for i in range(r_len):
    id, sub = result[i].split('*')
    id = n_dict[id]
    result[i] = id+sub
print(result)