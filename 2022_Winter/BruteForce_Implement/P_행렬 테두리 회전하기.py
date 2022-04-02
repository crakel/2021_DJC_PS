def solution(rows, columns, queries):
    num = 1
    mat = [[0] * columns for _ in range(rows)]
    answer = []

    for i in range(rows):
        for j in range(columns):
            mat[i][j] = num
            num += 1

    for query in queries:
        start = (query[0] - 1, query[1] - 1)
        end = (query[2] - 1, query[3] - 1)
        temp = mat[start[0]][start[1]]
        _min = [temp]
        # 좌변
        for x in range(start[0], end[0]):
            mat[x][start[1]] = mat[x+1][start[1]]
            _min.append(mat[x][start[1]])
            _min.append(mat[x+1][start[1]])
        # 하변
        for y in range(start[1], end[1]):
            mat[end[0]][y] = mat[end[0]][y+1]
            _min.append(mat[end[0]][y])
            _min.append(mat[end[0]][y+1])
        # 우변
        for x in range(end[0], start[0], -1):
            mat[x][end[1]] = mat[x-1][end[1]]
            _min.append(mat[x][end[1]])
            _min.append(mat[x-1][end[1]])
        # 상변
        for y in range(end[1], start[1], -1):
            mat[start[0]][y] = mat[start[0]][y-1]
            _min.append(mat[start[0]][y])
            _min.append(mat[start[0]][y-1])

        mat[start[0]][start[1]+1] = temp

        # for i in range(start[0], end[0] + 1):
        #     for j in range(start[1], end[1] + 1):
        #         if mat[i][j] < _min:
        #             _min = mat[i][j]
        # area = [row[start[0]:end[0]] for row in mat[start[1]:end[1]]]
        # for row in area:
        #     print(row)
        #     min_temp = min(row)
        #     if min_temp < _min:
        #         _min = min_temp
        answer.append(min(_min))
    return answer


# print(solution(4, 4, [[2, 2, 4, 4]]))
#print(solution(6, 6, [[2, 2, 5, 4]]))
# print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
# print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
#print(solution(3, 4, [[1, 1, 2, 2], [1, 2, 2, 3], [1, 3, 2, 4], [2, 3, 3, 4]]))
#print(solution(3, 5, [[1, 1, 2, 2], [2, 3, 3, 4]    , [1, 2, 3, 4], [1, 1, 3, 4], [2, 2, 3, 5]]))