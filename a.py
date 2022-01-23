import re
new_id = "......a......a......a....."
new_id = (new_id.lower())
new_id = re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', new_id)
#new_id = new_id.replace("..", ".")
new_id = list(new_id)
a = new_id[0]
i=0
while i != (len(new_id)-1):
    i=+1
    if (a == '.') & (new_id[i] == '.'):
        del new_id[i]
    a = new_id[i]
new_id = new_id.strip('.')
if len(new_id) == 0:
    new_id = ["a"]
new_id = list(new_id)
if len(new_id) >= 16:
    new_id = new_id[:15]
    if new_id[0] == '.':
        del new_id[0]
    if new_id[len(new_id)-1] == '.':
        del new_id[len(new_id)-1]
while len(new_id) < 3:
    new_id.append(new_id[len(new_id)-1])
answer = "".join(new_id)
print(answer)