people = [70,80,50,50]
limit = 100

people.sort()
answer = 0

a = 0
b = len(people) - 1
while a < b:
    if people[b] + people[a] <= limit:
        a += 1
        answer += 1
    b -= 1
print(len(people) - answer)