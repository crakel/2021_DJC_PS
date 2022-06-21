def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = int(''.join(numbers))

    return answer

print(solution([6, 10, 2]))             # result : 6210
print(solution([3, 30, 34, 5, 9]))      # result : 9534330
print(solution([0,0,0,0]))              # result : 0