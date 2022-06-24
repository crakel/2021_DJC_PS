def solution(clothes):
    answer = 0
    dic = {}
    for cloth in clothes:
        if cloth[1] in dic:
            dic[cloth[1]] += 1
        else:
            dic[cloth[1]] = 1

    cnt = 1
    for key in dic:
        # 입지않는 경우 포함 경우의 수
        cnt *= (dic[key] + 1)

    return cnt - 1 # 모두 안입는 것 제외
# 처음 시도 -> 전체 경우 못따짐
# def solution(clothes):
#     answer = 0
#     dic = {}
#     for cloth in clothes:
#         if cloth[1] in dic:
#             dic[cloth[1]].append(cloth[0])
#         else:
#             dic[cloth[1]] = [cloth[0]]
#
#     cnt = 0
#     for key, value in dic.items():
#         for v in value:
#             cnt += 1
#     print(cnt)
#     print(dic.items())
#     for a, b in zip(list(dic.items()), list(dic.items())[1:]):
#         cnt += (len(a[1]) * len(b[1]))
#
#     return cnt