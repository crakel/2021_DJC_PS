n = int(input())

res = [1] * n
a = list(map(int, input().split()))

# 1 4 5 2 3 4 5
for i in range(1, n): # 수열 끝나는 지점 LIS
    for j in range(i):
        if a[j] < a[i]:
            res[i] = max(res[i], res[j] + 1) # 이전의 가장 긴 수열 vs 현재 + 1

print(max(res))
