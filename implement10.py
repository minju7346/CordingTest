from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(len(weak)):
        weak.append(weak[i]+12)
    answer = len(dist) + 1
    for start in range(length):
        for friends in list(permutations(dist,len(dist))):
            count = 1
            position = weak[start] + friends[count-1]
            for index in range(start,start+length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer,count)
    if answer > len(dist):
        return -1
    return answer

solution(12,[1, 3, 4, 9, 10],[3, 5, 7])