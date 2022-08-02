s = ["h", "e", "l", "l", "o"]
slen = len(s)
for i in range(slen // 2):
    k = s[0 + i]
    s[0 + i] = s[slen - 1 - i]
    s[slen - 1 - i] = k
print(s)
