import sys
import heapq

n = int(sys.stdin.readline())
ppl = list(map(int, sys.stdin.readline().strip().split()))
adj = [[] * (n+1)]
print(adj)
for i in range(1, n+1):
    adj.append(list(map(int, sys.stdin.readline().strip().split())))
    del adj[i][0]

print(adj)