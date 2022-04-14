import sys

n, m = map(int, sys.stdin.readline().split())

field = []

for _ in range(n):
    field.append(list(map(int, sys.stdin.readline().split())))

print(field)

visit = [[0]*m for _ in range(n)]
print(visit)
_max = 0

# 좌 상 우 하
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, depth, total):
    global _max
    if depth == 4:
        print(total)
        if total > _max:
            _max = total
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if not visit[nx][ny]:
                total += field[nx][ny]
                visit[nx][ny] = 1
                dfs(nx, ny, depth+1, total)
                visit[nx][ny] = 0

    # for i in range(n):
    #     for j in range(m):
    #         if not visit[i][j]:
    #             total += field[i][j]
    #             visit[i][j] = 1
    #             dfs(depth+1, total)
    #             total = 0
    #             visit[i][j] = 0


for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 1, field[i][j])
        visit[i][j] = 0

print(_max)