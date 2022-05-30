import heapq


def solution(scoville, K):
    length = len(scoville)
    s = scoville
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) > 1:
        print(s)
        if min(s) >= K:
            return cnt
        a = heapq.heappop(s)
        b = heapq.heappop(s)
        new = a + b * 2
        heapq.heappush(s, new)
        cnt += 1

    return -1

solution([1,2,3,9,10,12], 7)