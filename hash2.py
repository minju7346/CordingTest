def solution(phone_book):
    answer = True
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        print(p1,p2)
    for i in range(len(phone_book)-1):
        k = len(phone_book)
        if phone_book[i] in phone_book[i+1][:k]:
            return False
    return answer

print(solution(["119", "97674223", "1195524421","1194"]))
string = "11234"
print(string.startswith("11"))