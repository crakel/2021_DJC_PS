import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
sum = 0
res = 0

while len(lst) > 0:
    min_p = min(lst)
    sum += min_p
    res += sum
    lst.pop(lst.index(min_p))

print(res)

