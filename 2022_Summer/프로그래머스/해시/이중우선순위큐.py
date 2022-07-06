import heapq


def solution(operations):
    answer = []
    min_h = []
    max_h = []
    for operation in operations:
        print(operation)
        o, n = operation.split()
        if o == "I":
            heapq.heappush(min_h, int(n))
            heapq.heappush(max_h, -int(n))
        else:
            if n == "1":
                heapq.heappop(max_h)
                tmp = []


            elif n == "-1":
                heapq.heappop(min_h)
    print(min_h)
    print(max_h)

    return answer

# print(solution(["I 16", "D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))