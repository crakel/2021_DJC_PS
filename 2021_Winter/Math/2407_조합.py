import sys

n, m = map(int, sys.stdin.readline().split())


def fac(n, end):
    if n > end:
        return n * fac(n - 1, end)

    else:
        return end


print(fac(n, n - m + 1) // fac(m, 1))

# itertools 시도 -> 너무 느림
# from itertools import combinations
#
# lst = [i for i in range(1, n+1)]
#
# print(len(list(combinations(lst, m))))
