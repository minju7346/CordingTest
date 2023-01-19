# 이진탐색은 최솟값과 최고값을 정하는 것을 생각하면서 알고리즘을 짠다
# 각 문제별 조건에 맞게 if문의 조건과 내부 추가된 변수들을 문제에 맞게 변형

def binary(start, end):
    global ans
    while start<=end:
        mid = (start+end)//2
        cur = arr[0]
        count = 1
        for i in range(1, len(arr)):
            if arr[i] >= cur+mid:
                count += 1
                cur = arr[i]
        if count >= C:
            start = mid+1
            ans = max(mid, ans)
        else:
            end = mid-1
    return ans

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
ans = 0
print(binary(1, arr[-1] - arr[0]))
