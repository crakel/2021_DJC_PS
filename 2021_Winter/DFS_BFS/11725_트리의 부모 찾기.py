import sys
from collections import deque

n = int(sys.stdin.readline())
graph = {}

for i in range(1, n+1):
    graph[i] = []

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


visit = [0] * (n+1)

def bfs(start):
    q = deque([start])
    while q:
        v = q.popleft()
        for w in graph[v]:
            if not visit[w]:
                visit[w] = v
                q.append(w)

bfs(1)
for v in visit[2:]:
    print(v)



# 시간초과 풀이
# def bfs(start):
#     found = []
#     q = deque([start])
#     while q:
#         v = q.popleft()
#         found.append(v)
#         if v == 1:
#             return found
#         for w in graph[v]:
#             q.append(w)
#
#
# for i in range(2, n+1):
#     print(bfs(i)[1])


