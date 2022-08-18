s=  "0P"
s = s.lower()
s = list(filter(str.isalnum, s))
slen = len(s)
return s == s[::-1]