# n m이 작고 시간제한이 2초니까 벽 3개를 무작정 구해봐도 되지않을까?
import sys
from collections import deque
from itertools import combinations
import copy

n, m = map(int, sys.stdin.readline().strip().split())

lab = []
for _ in range(n):
    lab.append(list(map(int, sys.stdin.readline().strip().split())))

# 0의 좌표값을 반환
def find_area(lab):
    safe_area = []
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                safe_area.append([i, j])
    return safe_area

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def bfs(lab):
    q = deque()
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2: # 아직 퍼지지않은 바이러스
                q.append([i, j])

            while q:
                cur_i, cur_j = q.popleft()

                for d in range(4):
                    ni = cur_i + di[d]
                    nj = cur_j + dj[d]
                    # 벽 탐색 방지
                    if ni < 0 or ni >= n or nj < 0 or nj >= m:
                        continue
                    if lab[ni][nj] == 0: # 바이러스 퍼짐
                        q.append([ni, nj])
                        lab[ni][nj] = 2

zeros = find_area(lab)
# 초기 0의 좌표값에서 3개 벽의 조합을 구한다
combi = list(combinations(zeros, 3))

max_area = 0

# 3개 벽의 좌표로 1을 넣어주고 복사생성된 연구소에서 0 갯수의 최대값을 구한다
for x in combi:
    tmp_lab = copy.deepcopy(lab)
    for i in range(3):
        tmp_lab[x[i][0]][x[i][1]] = 1
    bfs(tmp_lab)
    area_cnt = len(find_area(tmp_lab))
    if area_cnt > max_area:
        max_area = area_cnt

print(max_area)