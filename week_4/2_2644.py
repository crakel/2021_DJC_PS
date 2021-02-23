import sys
from collections import deque

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

g = [[0]*(n+1) for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
route = [0 for _ in range(n+1)]

# 인접행렬 입력
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    g[x][y] = g[y][x] = 1

# 시작부터 끝까지 경로?
def bfs(start, end):
    visit = [0 for _ in range(n+1)]
    visit[start] = 1

    q = deque()
    q.append(start)
    while q:
        cur_vertex = q.popleft()
        # end 경로 찾았다면 return 하고 종료 (조금이라도 시간이득..?)
        if g[cur_vertex][end] == 1:
            route[end] = route[cur_vertex] + 1
            return route[end]

        # 현재 vertex에서 가능한 인접 vertex 검사
        for i in range(1, n+1):
            if visit[i] == 0 and g[cur_vertex][i] == 1:
                q.append(i)
                visit[i] = 1
                route[i] = route[cur_vertex] + 1
    return -1

print(bfs(a,b))





