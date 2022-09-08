import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())

# 상 하 좌 우
dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# 방향
block = {
    '|': (0, 2),
    '-': (2, 3),
    '+': (0, 1, 2, 3),
    '1': (1, 4),
    '2': (0, 4),
    '3': (0, 3),
    '4': (3, 1),
    'M': (0, 1, 2, 3),
    'Z': (0, 1, 2, 3)
}

def bfs(r, c):
    # q = deque([])
    # q.append((r, c))
    # while q:
    #     nr, nc = q.popleft()
    #     visited[nr][nc] = 1
    #     dirs = block(field(r, c))
    pass
field = []
for i in range(r):
    field.append(list(sys.stdin.readline().strip()))

print(field)
for i in range(r):
    for j in range(c):
        if field[i][j] == 'M':
            m = (i, j)
        elif field[i][j] == 'Z':
            z = (i, j)

print(field)
print(m)
print(z)

visited = [[0] * c for _ in range(r)]

