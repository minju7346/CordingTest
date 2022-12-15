# 어떤 순서로 숫자 배열을 바꿔야지 차례대로 큰 숫자열이 나오나?
# 순열이 시간초과뜨면 조합도 고려해 볼 것
# 30의 배수가 될 수 밖에 없는 조건도 생각하기->모든 자리수 합이 3의 배수, 10의 배수임으로 0이 하나 있어야 함
from itertools import combinations
arr = input()
arr = sorted(arr, reverse=True)
for i in combinations(arr, len(arr)):
    if int(''.join(i)) % 30 == 0:
        print(int(''.join(i)))
        exit(0)
print(-1)