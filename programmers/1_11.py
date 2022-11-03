# 제한사항 수가 매우크고 효율성 점수가 있다면 이분탐색해보기
def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:  # 이분탐색의 while조건물
        temp = stones.copy()  # 더빠름
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:  # 오른쪽과 왼쪽포인터위치를 통해 수를 반으로 줄임
            right = mid - 1
        else:
            left = mid + 1

    return left