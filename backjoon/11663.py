from bisect import bisect_right, bisect_left
N, M = map(int, input().split())
nodes = list(map(int, input().split()))
lines = [list(map(int, input().split())) for _ in range(M)]
nodes.sort()
for l in lines:
    print(bisect_right(nodes, l[1])-bisect_left(nodes, l[0]))
