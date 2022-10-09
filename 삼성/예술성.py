from collections import deque

n = int(input())
# 상 하 좌 우
ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

def grouping():
    group = []
    visited = [[0] * n for _ in range(n)]
    def bfs(r, c, v):
        q = deque([(r, c)])
        cur_group = []
        while q:
            cr, cc = q.popleft()
            if grid[cr][cc] == v and not visited[cr][cc]:
                visited[cr][cc] = 1
                cur_group.append((cr, cc))
            for d in ds:
                nr, nc = cr + d[0], cc + d[1]
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    if grid[nr][nc] == v:
                        cur_group.append((nr, nc))
                        q.append((nr, nc))
                        visited[nr][nc] = 1
        if cur_group:
            group.append(cur_group)

    # 그룹 나누기
    for i in range(n):
        for j in range(n):
            bfs(i, j, grid[i][j])

    return group

# 예술 점수 계산
def cal_harmony():
    harmony = []
    group = grouping()
    for i in range(len(group)-1):
        for j in range(i+1, len(group)):
            g1 = group[i]
            g2 = group[j]

            g1_len = len(g1)
            g2_len = len(g2)
            g1_num = grid[g1[0][0]][g1[0][1]]
            g2_num = grid[g2[0][0]][g2[0][1]]
            adj = 0
            adj_visited = [[0] * n for _ in range(n)]
            for r, c in g1:
                # 맞닿아 있는 변 계산
                for d in ds:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) in g2:
                        adj += 1
            # for av in adj_visited:
            #     print(*av)
            # print(f'({g1_len} + {g2_len}) * {g1_num} * {g2_num} * {adj}')
            harmony.append((g1_len + g2_len) * g1_num * g2_num * adj)
    return sum(harmony)

def rotate():
    # 반시계 (십자값만 활용)
    cc_grid = list(map(list, reversed(tuple(zip(*grid)))))
    # 시계
    # ul, ur, dl, dr 4분할
    mid = n//2
    ul = list(map(list, zip(*reversed([*[r[:mid] for r in grid[:mid]]]))))
    ur = list(map(list, zip(*reversed([*[r[mid + 1:] for r in grid[:mid]]]))))
    dl = list(map(list, zip(*reversed([*[r[:mid] for r in grid[mid+1:]]]))))
    dr = list(map(list, zip(*reversed([*[r[mid+1:] for r in grid[mid+1:]]]))))

    for i in range(n):
        for j in range(n):
            if (i == mid) or (j == mid):
                grid[i][j] = cc_grid[i][j]
            # ul
            elif 0 <= i < mid and 0 <= j < mid:
                grid[i][j] = ul[i % (mid+1)][j % (mid+1)]
            # ur
            elif 0 <= i < mid and mid+1 <= j < n:
                grid[i][j] = ur[i % (mid+1)][j % (mid+1)]
            # dl
            elif mid+1 <= i < n and 0 <= j < mid:
                grid[i][j] = dl[i % (mid+1)][j % (mid+1)]
            # dr
            elif mid+1 <= i < n and mid+1 <= j < n:
                grid[i][j] = dr[i % (mid+1)][j % (mid+1)]


# 초기
r0 = cal_harmony()
# print(r0)
# for g in [row[:n//2] for row in grid[:n//2]]:
#     print(*g)
# 1회전
rotate()
r1 = cal_harmony()
# for g in grid:
#     print(*g)
# print(r1)
# 2회전
rotate()
r2 = cal_harmony()
# for g in grid:
#     print(*g)
# print(r2)
# 3회전
rotate()
r3 = cal_harmony()
# for g in grid:
#     print(*g)
#print(r3)

print(r0+r1+r2+r3)