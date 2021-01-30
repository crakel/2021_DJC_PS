n = list(input())

# stack = []
# cnt = []
#
# def push(list, x):
#     list.append(x)
#
#
# def pop(list):
#     res = list[-1]
#     del list[-1]
#     return res
#
# def top(list):
#     return list[-1]

num = ['2', '3', '4', '5', '6', '7', '8', '9']
res = [0] * 100 # 최대 길이 = 최대 깊이
mass = {'H':1, 'C':12, 'O':16}

i = 0 # 괄호의 깊이
for x in n:
    if x in mass:
        tmp = mass[x]
        res[i] += tmp

    elif x == '(':
        i+= 1
        res[i] = 0 # 뒤에 다시 새로운 괄호 나올때 이전 값 초기화

    elif x == ')':
        tmp = res[i]
        i-= 1
        res[i] += tmp

    elif x in num:
        res[i] += tmp * (int(x) - 1) # 앞에서 일단 더하고 봤으니 -1 곱

print(res[0])
