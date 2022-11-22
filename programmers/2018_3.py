from collections import deque
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
cacheSize = 2
result = 0
stack = deque(maxlen=cacheSize)
for i in cities:
    i = i.lower()
    if i not in stack:
        result += 5
        stack.append(i)
    else:
        result += 1
        stack.remove(i)
        stack.append(i)
print(result)
