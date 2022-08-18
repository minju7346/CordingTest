from collections import Counter
s= "leetcode"
counter = Counter(s)
for i, t in enumerate(s):
    if counter[t] == 1:
        print(i)
        exit(0)
print(-1)
