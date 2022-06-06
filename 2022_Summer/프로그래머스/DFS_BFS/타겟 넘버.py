answer = 0


# def solution(numbers, target):
#     def dfs(depth, total):
#         global answer
#         print("depth : ", depth)
#         print("total : ", total)
#         if depth == len(numbers):
#             if total == target:
#                 answer += 1
#             return
#
#         dfs(depth + 1, total + numbers[depth])
#         dfs(depth + 1, total - numbers[depth])
#
#     dfs(0, 0)
#     return answer


# 이해가 안되넴
def solution(numbers, target):
    def dfs(depth, visited, total):
        global answer
        print("depth : ", depth)
        if depth == len(numbers):
            if total == target:
                answer += 1
            return

        if not visited[depth]:
            visited[depth] = 1
            print("visited : ", visited)
            dfs(depth + 1, visited, total + numbers[depth])
            dfs(depth + 1, visited, total - numbers[depth])

    dfs(0, [0] * len(numbers), 0)
    return answer

print(solution([1,1,1,1,1], 3))