import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip().split()))

    if not heap:
        for num in row:
            heapq.heappush(heap, num)

    else:
        for num in row:
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)

print(heap[0])



# heapq를 사용하지 않고 풀어본 풀이 (왜 틀리지? 히든케이스 궁금)
# n = int(sys.stdin.readline())
# lst = []
# heap = []
#
# for _ in range(n):
#     lst.append(list(map(int, sys.stdin.readline().strip().split())))
#
# for i in range(n):
#     heap.append(lst[n-1][i])
#
# i = n
# while True:
#     if i == 1:
#         break
#
#     min_heap = min(heap)
#     min_index = heap.index(min_heap)
#     max_row = max(lst[i-2])
#     max_index = lst[i-2].index(max_row)
#     if min_heap < max_row:
#         heap[min_index] = max_row
#         lst[i-2][max_index] = 0
#     else:
#         i -= 1

# print(min(heap))
