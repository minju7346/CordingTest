from collections import Counter

s = "anagram"
t = "nagaram"
acnt = Counter(s)
tcnt = Counter(t)
if acnt == tcnt:
    print(True)
else:
    print(False)

