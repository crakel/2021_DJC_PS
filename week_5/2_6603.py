import sys
from itertools import combinations

comb = [0 for _ in range(13)]


def dfs(start, index):
    if index == 6:
        for i in range(6):
            print(comb[i], end=' ')
        print()
        return

    for i in range(start, k):
        comb[index] = s[i]
        dfs(i+1, index+1)


while True:
    s = list(map(int, sys.stdin.readline().strip().split()))
    k = s[0]
    if k == 0:
        break
    del s[0]
    # 순열 사용한 풀이
    # pick = list(combinations(s, 6))
    # for x in pick:
    #     print(*x)
    # 재귀 사용한 풀이
    dfs(0, 0)
    print()


