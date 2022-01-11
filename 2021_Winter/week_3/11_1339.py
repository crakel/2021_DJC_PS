# first idea
# 입력받는 문자를 리스트에넣고
# 리스트안에서 길이가 긴 순서대로(정렬) 리스트안의 문자하나하나 딕셔너리로 9부터 1까지 할당한다
# 그 후 리스트 요소끼리 딕셔너리를 이용해서 숫자로 변환후 더해준다

# second idea
# 생각해보니 최대값이 안될 경우 매우 많이 존재.. 길이가 기준이 아님
# 길이가 아니라 자릿수를 기준으로 딕셔너리 구성해서
# 제일 높은자리수를 가지는 수부터 9를 할당해주면 될 듯

import sys
word = []

n = int(sys.stdin.readline())


for i in range(n):
    word.append(sys.stdin.readline().strip())

allocate = {}
for i in range(n):
    for k, x in enumerate(word[i]):
        if x not in allocate:
            allocate[x] = 10 ** (len(word[i]) - 1 - k)
        else:
            allocate[x] += 10 ** (len(word[i]) - 1 - k)


sorted_allocate = sorted(allocate, key = lambda x:allocate[x], reverse=True)
# print(allocate)
num = 9
for x in sorted_allocate:
    allocate[x] = num
    num -= 1

res = 0
# print(allocate)
for i in range(n):
    word_num = ''
    for x in word[i]:
        word_num += str(allocate[x])
    res += int(word_num)

print(res)

