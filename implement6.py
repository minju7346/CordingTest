def solution(s):
    answer = 10000
    for step in range(1, len(s)//2+2):
        res = ''
        count = 1
        tmp = s[:step]
        for i in range(step, len(s)+step, step):
            if tmp == s[i:i+step]:
                count += 1
            else:
                if count == 1:
                    res += tmp
                else:
                    res + str(count) + tmp
                tmp = s[i:i+step]
                count = 1
        answer = min(answer, len(res))

    return answer


print(solution("ababcdcdababcdcd"))
