import sys

n = int(sys.stdin.readline())
parent = list(map(int, sys.stdin.readline().split()))
del_n = int(sys.stdin.readline())

tree = {}
leaf = 0

for i in range(n):
    tree[i] = parent[i]

print(tree)

tree[del_n] = -2


def del_node(node):
    for item, value in tree.items():
        if value == node:
            del_node(value)
            tree[item] = -2


del_node(del_n)


print(tree)


for i in range(n):
    is_leaf = True
    if tree[i] == -2:
        continue

    for item, value in tree.items():
        if value == i:
            is_leaf = False
            break
    if is_leaf:
        leaf += 1

print(leaf)