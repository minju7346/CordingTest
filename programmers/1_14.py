# 1. 투포인터로 합이 전체의 반이되는 구간 찾기
# 2. 마지막 인덱스 - 개수/2 + 시작인덱스 -> 얼마나 움직였는지 알아내는 공식

def solution(queue1, queue2):
    queue3 = queue1 + queue2
    chk_sum = sum(queue3)/2
    chk_len = len(queue3)
    s, e = 0, 0
    tmp_sum = queue3[0]
    while s < chk_len-1 and e < chk_len-1: # 탈출조건 만들어줘야함
        if tmp_sum == chk_sum:
            if e < chk_len/2-1:
                e += 1
                tmp_sum += queue3[e]
                continue
            return (s+e-int((chk_len)/2)+1)
        elif tmp_sum < chk_sum and e < chk_len -1:
            e += 1
            tmp_sum += queue3[e]
        elif tmp_sum > chk_sum:
            tmp_sum -= queue3[s]
            s += 1
    return -1
arr1 = [ 1, 1,8,2]
arr2 = [ 1,1, 1, 5]
print(solution(arr1, arr2))