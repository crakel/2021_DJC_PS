import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

lst = [i for i in range(1, n+1)]

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
        res.append(i+1)
        bt(depth+1)
        res.pop()

bt(0)

# 중복조합 풀이
# for k in list(itertools.product(lst, repeat=m)):
#     print(*k)