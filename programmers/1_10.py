#투포인트 -> 이중포문을 써야하는데 효율성이 중요할때 while문 하나로 해결하는 방법, 가변적이고 연속적인 배열구간으로 확인
gems = ["A","B","B","B","B","B","B","C","B","A"]
kind = len(set(gems))
N = len(gems)
answer = [0, N-1]
dic = {gems[0]:1}
l, r = 0, 0
while l<N and r<N:#둘 중 하나라도 크기를 넘어서면 종료
    if len(dic) < kind:#작으면 오른쪽을 늘림
        r += 1
        if r == N:
            break
        dic[gems[r]] = dic.get(gems[r], 0) + 1
    else: #종류개수와 같으면 왼쪽을 이동, answer과 비교후 갱신 및, 시작점 증가, 끝점 증가, 전 시작점 원소 삭제
        if r-l < answer[1]-answer[0]:
            answer = [l+1,r+1]
        if dic[gems[l]] == 1:#맨왼쪽 부분배열값이 1이면 삭제->딕셔너리이기때문에 조건문으로 삭제하거나 1을 줄이는 작업 진행
            del dic[gems[l]]
        else:#맨왼쪽외에도 있는 요소면 1 줄임
            dic[gems[l]] -= 1
        r += 1
print(answer[0], answer[1])