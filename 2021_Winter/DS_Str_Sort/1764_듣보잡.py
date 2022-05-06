import sys
from collections import defaultdict
n, m = map(int, sys.stdin.readline().split())

dic = defaultdict(int)

for _ in range(n+m):
    s = sys.stdin.readline().rstrip()
    dic[s] += 1

res = []
count = 0
for key, value in dic.items():
    if value == 2:
        res.append(key)
        count += 1

res.sort()
print(count)
print(*res, sep='\n') # unpacking operator *


