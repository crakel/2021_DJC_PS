import sys

n, m = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))


st = 0
ed = max(tree)

while st <= ed:
    mid = (st + ed) // 2

    sum_cut = 0
    for t in tree:
        if t >= mid:
            sum_cut += t - mid

    if sum_cut >= m:
        st = mid + 1

    elif sum_cut < m:
        ed = mid - 1

print(ed)