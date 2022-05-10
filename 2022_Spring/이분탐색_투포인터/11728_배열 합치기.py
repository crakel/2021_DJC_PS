import sys

n, m = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))


# 투 포인터 이용한 정렬
a, b = 0, 0
lst = []
while a != n or b != m:
    if a == n:
        lst.append(B[b])
        b += 1

    elif b == m:
        lst.append(A[a])
        a += 1

    else:
        if A[a] < B[b]:
            lst.append(A[a])
            a += 1

        else:
            lst.append(B[b])
            b += 1
print(*lst)

# 리스트 덧셈 이용 - 더 빠른이유 -> 파이썬 sort 내부적인 최적화 기법과 C언어 구현으로 인한 속도차이
# print(*sorted(A+B))