from itertools import *
from collections import *


def solution(orders, course):
    answer = []

    for n in course:
        able = []
        for order in orders:
            order = sorted(order)
            able.extend(list(combinations(order, n)))

        cnt = Counter(able)

        if cnt:
            max_cnt = max(cnt.values())

        if max_cnt >= 2:
            for key, value in cnt.items():
                if value == max_cnt:
                    answer.append(''.join(key))

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))


# 시간초과 코드
# def solution(orders, course):
#     answer = []
#     alp = {}
#     dic = defaultdict(list)
#
#     for order in orders:
#         for a in order:
#             if not a in alp:
#                 alp[a] = 1
#
#     for n in course:
#         for comb in combinations(sorted(list(alp.keys())), n):
#             cnt = 0
#             for order in orders:
#                 flag = 1
#                 for c in comb:
#                     if c not in list(order):
#                         flag = 0
#                         break
#
#                 if flag:
#                     cnt += 1
#
#             if cnt >= 2:
#                 tmp = '{}'.format(cnt)
#                 tmp += ''.join(comb)
#                 dic[n].append(tmp)
#
#     for key, value in dic.items():
#         value.sort(key=lambda x:(-int(x[0]), x[1:]))
#
#     for value in dic.values():
#         max_order = -1e9
#         for v in value:
#             if int(v[0]) >= max_order:
#                 max_order = int(v[0])
#                 answer.append(v[1:])
#             else:
#                 break

