n, m, k = map(int, input().split())
arr = map(int, input().split())
arr = list(set(arr))
arr = sorted(arr, reverse=True)
result += (m // (k+1))*arr[0]*k
result += (m - (m // (k+1))*k) * arr[1]
print(result)
