import math
def is_prime_number(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False
    return True
n = 110011
k = 10
a = ''
sum = 0
while n != 0:
    a = str(n%k) + a
    n = n//k
a = a.split('0')
print(a)
for i in a:#for문에서 탈출조건 달아서 시간 효율성을 올려줌
    if i == '' or int(i) < 2:
        continue
    if i.isdigit() and is_prime_number(int(i)):
        sum += 1
print(sum)