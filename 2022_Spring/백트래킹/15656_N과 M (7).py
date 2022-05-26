import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

lst = sorted(list(map(int, sys.stdin.readline().split())))

res = []
def bt():
    if len(res) == m:
        print(*res)
        return

    for i in range(n):
        res.append(lst[i])
        bt()
        res.pop()

bt()
# 중복조합 풀이
# for k in list(itertools.product(lst, repeat=m)):
#     print(*k)
