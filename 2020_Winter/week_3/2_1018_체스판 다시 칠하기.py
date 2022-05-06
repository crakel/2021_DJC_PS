n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(input())

min_list = []
for a in range(n-7):
    for b in range(m-7):
        # (0,0) 시작 2가지 경우
        case_w = 0
        case_b = 0

        # 8*8 검사 부분
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i + j) % 2 == 0:  # 시작좌표와 같아야하는 라인
                    if board[i][j] == 'W':
                        case_b += 1

                    else:
                        case_w += 1
                else:
                    if board[i][j] == 'W':
                        case_w += 1

                    else:
                        case_b += 1

        min_list.append(min(case_w, case_b))

print(min(min_list))