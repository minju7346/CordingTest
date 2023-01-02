from itertools import permutations

def calculator(cs):
    tot = nums[0]
    for idx, s in enumerate(cs):
        if s == '+':
            tot += nums[idx+1]
        elif s == '-':
            tot -= nums[idx + 1]
        elif s == '*':
            tot *= nums[idx + 1]
        else:
            if tot < 0:
                tot *= -1
                tot //= nums[idx + 1]
                tot *= -1
            else:
                tot //= nums[idx + 1]
    return tot

N = int(input())
nums = list(map(int, input().split()))
tmp = list(map(int, input().split()))
c = ['+','-','*','//']
cals = []
small, big = 1e9, -1e9
for idx, i in enumerate(tmp):
    for _ in range(i):
        cals.append(c[idx])

for cal in permutations(cals, N-1):
    t = calculator(cal)
    small = min(t, small)
    big = max(t, big)
print(big)
print(small)






