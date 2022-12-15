# 계속해서 젤 작은 값을 업데이트 해주면서 리스트가 변화할떄는 우선순위 큐 고려
import heapq

N = int(input())
hq = []
sum = 0
for _ in range(N): heapq.heappush(hq, int(input()))
for _ in range(N-1):
    num = heapq.heappop(hq) + heapq.heappop(hq)
    sum += num
    heapq.heappush(hq, num)
print(sum)

