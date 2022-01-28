def solution(people, limit):
    answer = 0
    a = 0
    b = len(people) - 1
    people.sort(reverse=True)
    while a < b:
        if people[a] + people[b] <= limit:
            a += 1
            b -= 1
        else:
            a += 1
        answer += 1
    if a == b:
        answer += 1
    return answer


print(solution([100, 500, 500, 900, 950], 1000))
