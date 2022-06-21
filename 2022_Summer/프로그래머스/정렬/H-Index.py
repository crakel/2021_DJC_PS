def solution(citations):
    citations.sort(reverse=True)
    for i, citation in enumerate(citations):
        if i >= citation:
            return i

print(solution([3, 0, 6, 1, 5]))