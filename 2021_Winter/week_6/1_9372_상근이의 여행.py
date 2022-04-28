import sys

t = int(sys.stdin.readline())

# 모든 국가가 연결되어있으므로 필요가 없는 과정 ㅠㅠ
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# def union_parent(parent ,a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())
    # parent = [0] * (n + 1)
    # edges = []
    # count = 0
    # for i in range(1, n + 1):
    #     parent[i] = i
    for __ in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        # edges.append([a, b])
        # for edge in edges:
        #     a, b = edge
        #     if find_parent(parent, a) != find_parent(parent, b):
        #         union_parent(parent, a, b)
        #         count += 1
    print(n-1)
