def solution(phone_book):
    # 딕셔너리 풀이
    dic = {}
    for phone_number in phone_book:
        dic[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in dic and temp != phone_number:
                return False
    return True

# def solution(phone_book):
#     # str 기본 sort 정렬 시 ASCII 코드로 -> 작은 숫자부터 비슷한 문자열 끼리 묶이게됨 (접두어)
#     phone_book.sort()

#     # zip함수 통해 두 개 짝으로 묶음 -> iterator로 phone_book 인덱스 변경됨
#     for a, b in zip(phone_book, phone_book[1:]):
#         if b.startswith(a):
#             return False
#     return True

# 효율성 실패 코드
# def solution(phone_book):
#     phone_book = sorted(phone_book, key=len)
#     answer = True
#
#     for i in range(len(phone_book)):
#         cur = phone_book[i]
#         for j in range(i + 1, len(phone_book)):
#             check = phone_book[j]
#
#             if (len(cur) < len(check)):
#                 check = check[:len(cur)]
#             elif (len(cur) > len(check)):
#                 cur = cur[:len(check)]
#
#             if cur == check:
#                 answer = False
#                 return answer
#
#     return answer