from collections import Counter
str1 = 'aa1+aa2'
str2 = 'AAAA12'
str1_set = []
str2_set = []
for i in range(len(str1)-1):
    if str1[i].isalpha() and str1[i+1].isalpha():
        str1_set.append(str1[i].lower()+str1[i+1].lower())
for i in range(len(str2)-1):
    if str2[i].isalpha() and str2[i + 1].isalpha():
        str2_set.append(str2[i].lower()+str2[i+1].lower())
inter = sum((Counter(str1_set)&Counter(str2_set)).values())
union = sum((Counter(str1_set)|Counter(str2_set)).values())
print(int(65536*(inter/union)))

