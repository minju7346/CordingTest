#1. user에서 banner별자리 맞춰서 이름 변경후 banner안에 있나 확인
#2. user 배열을 다 변형한 후 banner의 원소를 통해
#3. banner안에 같은 패턴있으면 그 수만큼 나눠주고 사전에 하나로 바꿔줌

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banner_id = ["*rodo", "*rodo", "******"]
answer = [0]*len(banner_id)
r = 1
for i in range(len(banner_id)):
    if i+1 < len(banner_id) and banner_id[i] in banner_id[i+1:]:
        del banner_id[i]
for banner in banner_id:
    a = []
    index = -1
    tmp = banner_id
    while True:
        index = banner.find('*', index + 1)
        if index == -1:
            break
        a.append(index)
    for user in user_id:
        for idx in a:
            user = user[:idx] + '*' + user[idx + 1:]
        print(user)
        if user in tmp:
            ban_idx = tmp.index(user)
            print(ban_idx, tmp)
            answer[ban_idx] += 1
            tmp[ban_idx] += '!'
result = 1
for i in answer:
    result *= i
print(answer)
print(result)

