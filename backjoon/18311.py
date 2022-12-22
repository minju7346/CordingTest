N, K = map(int, input().split())
arr = list(map(int, input().split()))
a = arr.copy()
arr.reverse()
a += arr

now = 0
for i, n  in enumerate(a):
    now += n
    if now > K:
        if i >= N:
            print(N-(i)%N)
        else:
            print((i+1)%N)
        break
