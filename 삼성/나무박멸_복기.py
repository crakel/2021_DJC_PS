N, M, K, C = map(int, input().split())

dir = [(-1,0),(1,0),(0,-1),(0,1)]
# 상 하 좌 우

field = []
for _ in range(N):
    field.append(list(map(int, input().split())))


def check_range(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True

    else:
        return False

def day():
    for r in range(N):
        for c in range(N):
            if fire_ing[r][c] < 0:
                fire_ing[r][c] += 1


def job_grow():
    for r in range(N):
        for c in range(N):
            if field[r][c] > 0:
                job_cnt = 0
                for d in dir:
                    nr, nc = r + d[0], c + d[1]
                    if check_range(nr, nc) and field[nr][nc] > 0:
                        job_cnt += 1
                field[r][c] += job_cnt


def job_spread():
    spread = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if field[r][c] > 0:
                spread_cnt = 0
                spread_lst = []
                for d in dir:
                    nr, nc = r + d[0], c + d[1]
                    if check_range(nr, nc) and field[nr][nc] == 0 and fire_ing[nr][nc] == 0:
                        spread_cnt += 1
                        spread_lst.append((nr, nc))

                for sl in spread_lst:
                    spread[sl[0]][sl[1]] += field[r][c] // spread_cnt

    # 번식 동기화
    for r in range(N):
        for c in range(N):
            if field[r][c] == 0 and fire_ing[r][c] == 0:
                field[r][c] += spread[r][c]


def fire(fire_field):
    global total_fire_cnt
    for r in range(N):
        for c in range(N):
            if fire_field[r][c] == 1 and field[r][c] >= 0:
                # if fire_ing[r][c] <= 0:
                #     fire_ing[r][c] -= (C + 1)
                if fire_ing[r][c] <= 0:
                    fire_ing[r][c] = -(C+1)
                # else:
                #     fire_ing[r][c] = C
                total_fire_cnt += field[r][c]
                field[r][c] = 0

def is_empty():
    for r in range(N):
        for c in range(N):
            if field[r][c] > 0:
                return False

    return True


def fire_spread(r, c, k):
    fire_lst = [[0] * N for _ in range(N)]

    fire_lst[r][c] = 1
    if field[r][c] == 0:
        # for f in fire_lst:
        #     print(f)
        return fire_lst

    ul = [r, c]
    ur = [r, c]
    dl = [r, c]
    dr = [r, c]

    ul_flag = 0
    ur_flag = 0
    dl_flag = 0
    dr_flag = 0

    for _ in range(k):
        if check_range(ul[0]-1, ul[1]-1) and not ul_flag:
            ul = [ul[0]-1, ul[1]-1]

        if check_range(ur[0]-1, ur[1]+1) and not ur_flag:
            ur = [ur[0]-1, ur[1]+1]

        if check_range(dl[0]+1, dl[1]-1) and not dl_flag:
            dl = [dl[0]+1, dl[1]-1]

        if check_range(dr[0]+1, dr[1]+1) and not dr_flag:
            dr = [dr[0]+1, dr[1]+1]

        if field[ul[0]][ul[1]] <= 0:
            ul_flag = 1
            if field[ul[0]][ul[1]] == 0:
                fire_lst[ul[0]][ul[1]] = 1
        else:
            fire_lst[ul[0]][ul[1]] = 1

        if field[ur[0]][ur[1]] <= 0:
            ur_flag = 1
            if field[ur[0]][ur[1]] == 0:
                fire_lst[ur[0]][ur[1]] = 1
        else:
            fire_lst[ur[0]][ur[1]] = 1

        if field[dl[0]][dl[1]] <= 0:
            dl_flag = 1
            if field[dl[0]][dl[1]] == 0:
                fire_lst[dl[0]][dl[1]] = 1
        else:
            fire_lst[dl[0]][dl[1]] = 1

        if field[dr[0]][dr[1]] <= 0:
            dr_flag = 1
            if field[dr[0]][dr[1]] == 0:
                fire_lst[dr[0]][dr[1]] = 1
        else:
            fire_lst[dr[0]][dr[1]] = 1

    return fire_lst


def cnt_fire_spread(k):
    for r in range(N):
        for c in range(N):
            if field[r][c] != -1:
                fire_field = fire_spread(r, c, k)
                fire_cnt = 0
                for i in range(N):
                    for j in range(N):
                        if fire_field[i][j] == 1 and field[i][j] > 0:
                            fire_cnt += field[i][j]

                can_fire_spread.append((fire_cnt, r, c))

for f in field:
    print(f)

total_fire_cnt = 0
total_fire = 0
fire_ing = [[0] * N for _ in range(N)]

for i in range(M):
    day()

    if is_empty():
        continue

    print("불상태")
    for fi in fire_ing:
        print(fi)
    print()
    #print(fire_ing)[필수문항] 자신에 대해 자유롭게 표현해 주세요.


    job_grow()
    print("성장")
    for f in field:
        print(f)
    print()

    job_spread()
    print("번식")
    for f in field:
        print(f)
    print()

    can_fire_spread = []
    cnt_fire_spread(K)
    can_fire_spread.sort(reverse=True, key=lambda x : (x[0],-x[1],-x[2]))
    print(can_fire_spread)
    if len(can_fire_spread) > 0:
        fire_field = fire_spread(can_fire_spread[0][1], can_fire_spread[0][2], K)
        print("최대 불영역")
        for ff in fire_field:
            print(ff)
        print()
        # total_fire += can_fire_spread[0][0]
        fire(fire_field)

#print(total_fire)
print(total_fire_cnt)