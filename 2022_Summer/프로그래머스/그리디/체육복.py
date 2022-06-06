def solution(n, lost, reserve):
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)

    for r in _reserve:
        left = r - 1
        right = r + 1
        if left in _lost:
            _lost.remove(left)

        elif right in _lost:
            _lost.remove(right)

    answer = n - len(_lost)
    return answer
# 틀린 풀이
# def solution(n, lost, reserve):
#     answer = n - len(lost)
#     for l in lost:
#         left = l - 1
#         right = l + 1
#         print(reserve)
#         for r in reserve:
#             if r == l:
#                 reserve.remove(r)
#                 answer += 1
#                 break
#
#         for r in reserve:
#             if r == left or r == right:
#                 reserve.remove(r)
#                 answer += 1
#                 break
#     return answer