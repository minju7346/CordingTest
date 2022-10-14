s=  "0P"
# s = s.lower()
new = ""
for i in s:
    if i.isalpha():
        new += i.lower()
#list로 만드는 것보다 문자열로 다시 새로운것 만드는게 메모리 효율적임
slen = len(s)
return s == s[::-1]