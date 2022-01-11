# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:13:58 2022

@author: minju
"""

import re
new_id = "......a......a.{..[...a....."
new_id = (new_id.lower())
new_id = re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>\{\}`\'…》]', '', new_id)
new_id = list(new_id)
a = new_id[0]
i=1
while i < len(new_id):
    if (a == '.') & (new_id[i] == '.'):
        del new_id[i]
        i -= 1
    a = new_id[i]
    i+= 1
new_id = "".join(new_id)
new_id = new_id.strip('.')
new_id = list(new_id)
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