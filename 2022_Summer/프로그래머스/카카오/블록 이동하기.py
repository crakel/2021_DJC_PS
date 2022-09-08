from collections import deque

# 상 하 좌 우
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(board):
    answer = 0

    # 회전축 고려
    robot = [[0, 0], [0, 1]]

    # 가로 to 세로

    # 세로 to 가로
    return answer

# type 0 가로 type 1 세로 상태
def rot(axis, type):
    pass


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))