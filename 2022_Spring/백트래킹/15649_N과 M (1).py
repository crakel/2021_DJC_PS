import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

lst = [i for i in range(1, n+1)]
visited = [0 for _ in range(n)]

# 백트래킹 풀이
res = []
def bt(depth):
    # print("lst : ", lst)
    # print("visited", visited)
    # print()
    if depth == m:
        print(*res)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            res.append(i+1)
            bt(depth+1)
            visited[i] = 0
            res.pop()

bt(0)


# 순열 풀이
# for k in list(itertools.permutations(lst, m)):
#     print(*k)