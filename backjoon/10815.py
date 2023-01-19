M = int(input())
marr = list(map(int, input().split()))
N = int(input())
narr = list(map(int, input().split()))
marr.sort()
def binary(start, end, target):
    while start<=end:
        mid = (start+end)//2
        if marr[mid] == target:
            return 1
        elif marr[mid] < target:
            start = mid+1
        else:
            end = mid -1
    return 0
for i in narr:
    print(binary(0,M,i), end=" ")
