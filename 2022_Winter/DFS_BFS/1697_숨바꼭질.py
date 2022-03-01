import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
if n >= k:
    print(n-k)
    exit(0)

dp = [0] * 2 * k


def bfs(start, end):
    q = deque([start])
    while q:
        v = q.popleft()
        if v == end:
            print(dp[v])
            break
        for path in [v-1, v+1, v*2]:
            if 0 <= path <= 2 * end and not dp[path]:
                dp[path] = dp[v] + 1
                q.append(path)

bfs(n, k)
print(dp)
# 오답 (반례 못찾음)
# N=15,K=29 ans=2 는 맞음
# graph = {}
# for i in range(n, k+2):
#     graph[i] = []
#     if i-1 >= n:
#         graph[i].append(i-1)
#     if i+1 <= k+2:
#         graph[i].append(i+1)
#     if 2*i <= k+2:
#         graph[i].append(2*i)
#
#
# path = []
# def bfs(start, end):
#     visit = [start]
#     q = deque([start])
#     while q:
#         v = q.popleft()
#         path.append(v)
#         for w in graph[v]:
#             if w == end:
#                 return
#
#             if w not in visit:
#                 visit.append(w)
#                 q.append(w)
#
#
# bfs(n, k)
#
# tmp = path[-1]
# res = [tmp]
# for i in range(len(path)-1, -1, -1):
#     if path[i]-1==tmp or path[i]+1==tmp or path[i]*2==tmp:
#         res.append(path[i])
#         tmp = path[i]
#
# print(len(res))


