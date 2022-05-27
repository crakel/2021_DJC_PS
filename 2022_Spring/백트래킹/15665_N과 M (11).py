import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

lst = sorted(list(set(map(int, sys.stdin.readline().split()))))
res = []

# 백트래킹 구현
def bt():
    if len(res) == m:
        print(*res)
        return

    for i in range(len(lst)):
        res.append(lst[i])
        bt()
        res.pop()

bt()

# 조합 풀이
# for l in itertools.product(lst, repeat=m):
#     print(*l)