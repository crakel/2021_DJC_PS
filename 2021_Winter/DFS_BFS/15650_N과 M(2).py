import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())

lst = [i for i in range(1, n+1)]

for i in combinations(lst, m):
    for j in i:
        print(j, end=' ')
    print('')


# DFS 백트래킹 풀이
# def dfs(start):
#     if len(lst) == m:
#         print(''.join(map(str, lst)))
#         return
#
#     for i in range(start, n+1):
#         if i not in lst:
#             lst.append(i)
#             dfs(i+1)
#             lst.pop()
#
#
# dfs(1)