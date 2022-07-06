from collections import deque

def solution(genres, plays):
    answer = []
    dic = {}
    for i, genre in enumerate(genres):
        if genre not in dic:
            dic[genre] = [plays[i], deque([(plays[i], i)])]
        else:
            dic[genre][0] += plays[i]
            dic[genre][1].append((plays[i], i))
    print(dic)
    lst = list(dic.items())
    lst.sort(key=lambda x:-x[1][0])
    for k in lst:
        k[1][1] = deque(sorted(k[1][1], key=lambda x:(-x[0],x[1])))

    for n in lst:
        if len(n[1][1]) == 1:
            a = n[1][1].popleft()
            answer.append(a[1])
        else:
            a, b = n[1][1].popleft(), n[1][1].popleft()
            answer.append(a[1])
            answer.append(b[1])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

# heap 구현
#import heapq

# def solution(genres, plays):
#     answer = []
#     dic = {}
#     for i, genre in enumerate(genres):
#         if genre not in dic:
#             dic[genre] = [plays[i], [(-plays[i], i)]]
#         else:
#             dic[genre][0] += plays[i]
#             heapq.heappush(dic[genre][1], (-plays[i], i))
#     print(dic)
#     lst = list(dic.items())
#     lst.sort(key=lambda x:x[1][1])
#     print(lst)
#     for n in lst:
#         if len(n[1][1]) == 1:
#             answer.append(n[1][1][0][1])
#         else:
#             a, b = heapq.heappop(n[1][1]), heapq.heappop(n[1][1])
#             if a[0] == b[0]:
#                 if a > b:
#                     answer.append(b[1])
#                     answer.append(a[1])
#             else:
#                 answer.append(a[1])
#                 answer.append(b[1])
#     return answer
#
# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

