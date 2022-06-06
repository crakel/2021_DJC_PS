import itertools


def solution(n, times):
    left = 1
    right = max(times) * n
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        # 조건 검사
        for time in times:
            cnt += mid // time

        # 최적의 값을 찾기 위해 계속 좁혀나감
        if cnt >= n:
            answer = mid
            right = mid - 1

        else:
            left = mid + 1
    return answer
from itertools import combinations
# 그냥 구현 (시간초과)
# def solution(n, times):
#     wait = n
#     t = 0
#     while wait:
#         t += 1
#         for time in times:
#             if t % time == 0:
#                 wait -= 1
#
#     return t