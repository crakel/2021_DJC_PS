n = int(input())

col = [ None ] * n
queen_count = 0


def isPromise(col, i):
    j = 0
    flag = True
    while j < i and flag:
        if col[i] == col[j] or abs(col[i] - col[j]) == (i - j):
            flag = False
        j += 1
    return flag


def dfs(col, i):
    global queen_count
    if i == n:
        queen_count += 1

    else:
        for j in range(n):
            col[i] = j
            if isPromise(col, i):
                dfs(col, i + 1)


dfs(col, 0)
print(queen_count)


