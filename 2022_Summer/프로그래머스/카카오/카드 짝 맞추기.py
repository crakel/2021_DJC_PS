from itertools import *
from collections import *

# 상 하 좌 우
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def area_able(board, r, c):
    if not 0 <= r < 4 or not 0 <= c < 4 or board[r][c] != 0:
        return False
    return True


def move(d, r, c):
    nr, nc = r + dir[d], c + dir[d]
    if area_able(nr, nc):
        return nr, nc
    else:
        return False


def ctrl_move(d, r, c):
    nr, nc = r, c
    while True:
        if not area_able(nr, nc):
            return nr, nc
        else:
            nr, nc = nr + dir[d], nc + dir[d]

# 최단경로 -> bfs 생각

def solution(board, r, c):
    answer = 0
    cards = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                cards[board[i][j]].append((i, j))
    print(cards)
    routes = list(permutations(cards.keys()))
    print(routes)
    for route in routes:

    return answer

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))